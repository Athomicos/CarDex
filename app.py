import datetime
import os
from PIL import Image, ImageOps
import uuid

from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, kmh, cv, login_required, get_user_collection

app = Flask(__name__)

app.jinja_env.filters["kmh"] = kmh
app.jinja_env.filters["cv"] = cv

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(24)
Session(app)

# Config for upload photos
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB limit
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cardex.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Main menu"""
    return render_template("index.html")


@app.route("/add_car", methods=["GET", "POST"])
@login_required
def add_car():
    """Add a car"""
    if request.method == "POST":
        id = request.form.get("version_id")

        if not id:
            return apology("must provide a car version", 400)

        existing = db.execute("SELECT * FROM sightings WHERE user_id = ? AND car_id = ?", session["user_id"], id)

        if existing:
            return apology("you already have this car in your collection", 409)

        if not db.execute("SELECT * FROM cars WHERE id = ?", id):
            return apology("invalid car version", 400)
        
        location = request.form.get("ubicacion")
        date = datetime.date.today()

        photo = request.files.get("fotos")
        photo_path = save_photo(photo)

        if photo_path == "ERROR":
            return apology("invalid photo format", 400)

        db.execute("""INSERT INTO sightings (user_id, car_id, date, location, photo_path) 
                   VALUES (?, ?, ?, ?, ?)""", session["user_id"], id, date, location, photo_path)

        return redirect("/")

    else:
        brands = db.execute("SELECT DISTINCT brand FROM cars ORDER BY brand ASC")
        return render_template("add_car.html", brands=brands)

@app.route("/collection")
@login_required
def collection():
    """Show user's collection"""
    user_id = session["user_id"]

    user_cars = get_user_collection(user_id)

    return render_template("collection.html", user_cars=user_cars)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)

        if not request.form.get("password"):
            return apology("must provide password", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["password_hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not name:
            return apology("must provide username", 400)

        if not password:
            return apology("must provide password", 400)

        if not confirmation:
            return apology("must provide password confirmation", 400)

        if password != confirmation:
            return apology("passwords do not match", 400)

        for username in db.execute("SELECT username FROM users"):
            if username["username"].lower() == name.lower():
                return apology("username already exists", 409)

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", name, hash)
            return redirect("/login")
        except ValueError or RuntimeError:
            return apology("error registering user", 404)

        
    else:
        return render_template("register.html")


@app.route("/models/<brand>")
@login_required
def models(brand):
    modelos = db.execute("SELECT DISTINCT model FROM cars WHERE brand = ?", brand)
    return jsonify(modelos)


@app.route("/versions/<brand>/<model>")
@login_required
def versions(brand, model):
    versions = db.execute("SELECT id, version FROM cars WHERE brand = ? AND model = ? AND id NOT IN (SELECT car_id FROM sightings WHERE user_id = ?)", brand, model, session["user_id"])
    return jsonify(versions)


def save_photo(photo):
    """Save uploaded photo and return the file path."""
    if not photo or photo.filename == "":
        return None

    try:
        img = Image.open(photo)
        img.verify()  # Verify that it's an image
    except Exception as e:
        return "ERROR"

    photo.seek(0)
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)  # Correct orientation based on EXIF data
    img.thumbnail((1024, 1024))  # Resize to a maximum of 1024x1024

    name = f"{uuid.uuid4().hex}.jpg"
    path = os.path.join(UPLOAD_FOLDER, name)
    img.convert("RGB").save(path, "JPEG", quality=85)  # Save as JPEG

    return path


@app.route("/car/<id>")
@login_required
def car_detail(id):
    car_info = db.execute("""
        SELECT
            cars.*,
            sightings.photo_path,
            sightings.date,
            sightings.location
        FROM cars
        JOIN sightings ON cars.id = sightings.car_id
        WHERE sightings.user_id = ? AND cars.id = ?
    """, session["user_id"], id)

    if not car_info:
        return apology("car not found in your collection", 404)

    return render_template("car_detail.html", car=car_info[0])


@app.route("/search_car")
@login_required
def search_car():
    user_id = session["user_id"]
    
    user_cars = get_user_collection(user_id)

    return render_template("search_car.html", user_cars=user_cars)
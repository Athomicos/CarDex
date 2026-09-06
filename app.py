import os

from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, kmh, cv, login_required

app = Flask(__name__)

app.jinja_env.filters["kmh"] = kmh
app.jinja_env.filters["cv"] = cv

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(24)
Session(app)

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


@app.route("/add_car")
@login_required
def add_car():
    """Add a car"""
    if request.method == "POST":
        pass

    else:
        brands = db.execute("SELECT * FROM cars ORDER BY brand ASC")
        return render_template("add_car.html", brands=brands)

@app.route("/collection")
@login_required
def collection():
    """Show user's collection"""
    return render_template("collection.html")


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
            return apology("invalid username and/or password", 400)

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
                return apology("username already exists", 400)

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", name, hash)
            print("Yippie")
            return redirect("/login")
        except ValueError as e:
            print(e)
            return apology("error registering user", 400)

        
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
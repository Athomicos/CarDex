import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
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
db = SQL("sqlite:///carspot.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
# @login_required
def index():
    """Main menu"""
    return render_template("index.html")


@app.route("/add_car")
# @login_required
def add_car():
    """Add a car"""
    return render_template("add_car.html")

@app.route("/collection")
# @login_required
def collection():
    """Show user's collection"""
    return render_template("collection.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")


@app.route("/register")
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        if not name:
            return apology("must provide username", 400)

        if not password:
            return apology("must provide password", 400)

        if password != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        for username in db.execute("SELECT nombre_usuario FROM users"):
            if username["nombre_usuario"].tolower() == name.tolower():
                return apology("username already exists", 400)

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (nombre_usuario, password_hash) VALUES (?, ?)", name, hash)
            return redirect("/login")
        except ValueError:
            return apology("error registering user", 400)

        
    else:
        return render_template("register.html")
import os

from cs50 import SQL
from flask import Flask
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
@login_required
def index():
    """Main menu"""
    return apology("Nothing at the moment")


@app.route("/add_car")
@login_required
def add_car():
    """Add a car"""
    return apology("Nothing at the moment")


@app.route("/collection")
@login_required
def collection():
    """Show user's collection"""
    return apology("Nothing at the moment")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    return apology("Nothing at the moment")


@app.route("/logout")
def logout():
    """Log user out"""
    return apology("Nothing at the moment")


@app.route("/register")
def register():
    """Register user"""
    return apology("Nothing at the moment")
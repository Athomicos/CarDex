import requests

from cs50 import SQL
from flask import redirect, render_template, session
from functools import wraps

db = SQL("sqlite:///cardex.db")

def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", top=code, bottom=message), code


def kmh(value):
    """Format value as kilometers per hour."""
    return f"{value:.1f} km/h"


def cv(value):
    """Format value as horsepower."""
    return f"{value:.1f} cv"



def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def get_user_collection(user_id):
    user_cars = db.execute("""
            SELECT
                cars.*,
                sightings.photo_path,
                sightings.date,
                sightings.location
            FROM cars
            JOIN sightings ON cars.id = sightings.car_id
            WHERE sightings.user_id = ? ORDER BY sightings.date DESC
        """, user_id)

    return user_cars
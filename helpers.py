import requests

from flask import redirect, render_template, session
from functools import wraps

def kmh(value):
    """Format value as kilometers per hour."""
    return f"{value:.1f} km/h"

def cv(value):
    """Format value as horsepower."""
    return f"{value:.1f} cv"
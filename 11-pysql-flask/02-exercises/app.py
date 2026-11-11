from flask import Flask
from flask import render_template
from flask import request

from database import get_cities
from database import get_countries

from mysql.connector import Error

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
        return render_template("index.html", heading = "Woop woop woop!")

@app.route("/about")
def about():
        return render_template("about.html", author="Henriette Grindheim")

@app.route("/greet")
def greet():
        name = request.args.get("name", "Guest").strip().upper()
        return render_template("greet.html", name=name)

@app.route("/cities")
def cities():
        code = request.args.get("country", "NOR").strip().upper()
        if (len(code)) != 3 or not code.isascii() or not code.isalpha():
                return "Invalid code", 400

        try:
                rows = get_cities(code)
        except Error:
                app.logger.exception("Database query failed")
                return "Database unavailable", 503
        count = len(rows)
        return render_template("cities.html", code=code, rows=rows, count=count)

@app.route("/countries")
def countries():
        region = request.args.get("region", "Southern Europe").strip()
        if not region:
                return "Invalid region", 400

        try:
                rows = get_countries(region)
        except Error:
                app.logger.exception("Database query failed")
                return "Database unavailable", 503
        count = len(rows)
        return render_template("countries.html", region=region, rows=rows, count=count)
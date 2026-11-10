from flask import Flask
from flask import render_template
from flask import request

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
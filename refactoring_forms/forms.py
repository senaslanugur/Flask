from app import app
from flask import Flask, render_template
import forms


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", current_title="Home Custom Title")


@app.route("/about")
def about():
    form = forms.AddTaskForm()
    return render_template("about.html", current_title="About Custom Title", form = form)
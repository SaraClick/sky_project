from flask import render_template
from application import app
from application.python_scripts.data_provider_service import DataProviderService

DATA_PROVIDER = DataProviderService()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/content_media")
def content_media():
    return render_template("content_media.html")


@app.route("/content_selection")
def content_selection():
    return render_template("content_selection.html")


@app.route("/tips")
def tips():
    return render_template("tips.html")

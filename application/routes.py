from flask import render_template
from application import app
from application.python_scripts.data_provider_service import DataProviderService


DATA_PROVIDER = DataProviderService()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

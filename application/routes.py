from flask import render_template, request
from application import app
from application.python_scripts.data_provider_service import DataProviderService
from application.forms.forms import TypeForm, CategoryForm



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


@app.route("/select_type", methods=['GET', 'POST'])
def content_selection_type():
    user_type = None
    form = TypeForm()

    # If there is a submit (aka POST of the form) the below checks will be executed.
    if form.validate_on_submit():
        if form.data["submit_sound"]:
            user_type = "sound"
        if form.data["submit_video"]:
            user_type = "video"
        return user_type

    # If no post method it will render the selection category html file
    return render_template("content_selection_type.html", form=form)


@app.route("/select_category", methods=['GET', 'POST'])
def content_selection_category():
    form = CategoryForm()
    user_category = None
    # If there is a submit (aka POST of the form) the below checks will be executed.
    if form.validate_on_submit():
        if form.data["submit_wave"]:
            user_category = "wave"
        elif form.data["submit_rain"]:
            user_category = "rain"
        elif form.data["submit_whale"]:
            user_category = "whale"
        elif form.data["submit_brown_noise"]:
            user_category = "brown noise"
        elif form.data["submit_white_noise"]:
            user_category = "white noise"
        elif form.data["submit_instrumental"]:
            user_category = "instrumental"
        return user_category
    # If no post method it will render the selection category html file
    return render_template("content_selection_category.html", form=form)


@app.route("/tips")
def tips():
    return render_template("tips.html")

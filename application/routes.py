from flask import render_template, request
from application import app
from application.python_scripts.data_provider_service import DataProviderService
from application.forms.forms import SoundForm



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


@app.route("/content_selection", methods=['GET', 'POST'])
def content_selection():
    user_type = None
    user_category = None
    form = SoundForm()
    # Empty variables to store the user selection from type/category clickable buttons
    # POST to be executed upon user clicking a type

    if form.validate_on_submit():
        if form.data["submit_sound"]:
            user_type = "sound"
            return user_type
        if form.data["submit_video"]:
            user_type = "video"
            return user_type

    if request.method == 'GET':
        return render_template("content_selection.html", form=form)


@app.route("/tips")
def tips():
    return render_template("tips.html")

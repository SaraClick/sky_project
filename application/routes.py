from flask import render_template, request, redirect, url_for
from application import app
from application.python_scripts.data_provider_service import DataProviderService
from application.forms.forms import TypeForm, CategoryForm, MediaOutputForm
from random import choice

DATA_PROVIDER = DataProviderService()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/select_type", methods=['GET', 'POST'])
def content_selection_type():
    user_type = None  # empty variable to store the user's type selection
    form = TypeForm()  # instantiate form

    # If there is a submit (aka POST of the form) the below checks will be executed.
    # Each button has been set as a submit button, by clicking on the button, the user_type variable will be assigned
    # a string "sound" or "video
    if form.validate_on_submit():
        if form.data["submit_sound"]:
            user_type = "sound"
        if form.data["submit_video"]:
            user_type = "video"
        # redirect will execute the function inside the url_for(). User type selected on content_selection_type()
        # is being passed as a named parameter so we can end up using it in the final screen content_media()
        return redirect(url_for("content_selection_category", type_p=user_type))

    # If no post method it will render the selection category html file
    return render_template("content_selection_type.html", form=form)


@app.route("/select_category", methods=['GET', 'POST'])
def content_selection_category():
    form = CategoryForm()  # instantiate form
    user_category = None  # empty variable to store the user's type selection
    user_type = request.args.get("type_p")  # named variable stored when select_type was rendered

    # If there is a submit (aka POST of the form) the below checks will be executed.
    # Each button has been set as a submit button, by clicking on the button, the user_category variable will be
    # assigned a string value with the name of the clicked category
    if form.validate_on_submit():
        if form.data["submit_ocean"]:
            user_category = "ocean"
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
        # redirect will execute the function inside the url_for(). User type/category selected on
        # content_selection_type() and content_selection_category() will be passed as a named parameters so we can
        # use them in the redirected function content_media()
        return redirect(url_for("content_media", type_p=user_type, category_p=user_category))

    # If no post method it will render the selection category html file
    return render_template("content_selection_category.html", form=form)


@app.route("/content_media", methods=['GET', 'POST'])
def content_media():
    form = MediaOutputForm()  # instantiate form

    user_type1 = request.args.get("type_p")  # named parameter from content_selection_type() and passed onto content_selection_category()
    user_category = request.args.get("category_p")  # named parameter from content_selection_category()

    # Using method to execute select query from MySQL to retrieve the urls matching the type and category from the named parameters
    list_url = DATA_PROVIDER.get_url(user_type1, user_category)
    # selected_url is a variable to store a random URL selected from list_url. For this we have imported "random" and
    # will be using the method choice(list).
    # choice(list) → returns a random item from a sequence (aka list, tuple, string, or any iterable like range)
    selected_url = choice(list_url)
    # We use render template nd named parameters, the named parameters are used within the Jinja code to specify the
    # type (so we know if we have to use YouTube or Spotify iframe) and the URL to be passed into the iframe

    if form.validate_on_submit():
        # If user hits "Select another video/audio" it calls returns the function again
        if form.data["submit_new_media"]:
            return render_template("content_media.html", user_type=user_type1, media_url=selected_url, form=form)

    return render_template("content_media.html", user_type=user_type1, media_url=selected_url, form=form)


@app.route("/tips")
def tips():
    return render_template("tips.html")


@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")
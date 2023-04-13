from flask import render_template, request, redirect, url_for
from application import app
from application.python_scripts.data_provider_service import DataProviderService
from application.forms.forms import TypeForm, CategoryForm
from application.python_scripts.utils import select_random_from_list

DATA_PROVIDER = DataProviderService()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/content_media", methods=['GET', 'POST'])
def content_media(type='video', selected_url="https://www.youtube.com/embed/JmEGknad17w"):
    # Testing examples
    # type='sound', selected_url)="https://open.spotify.com/embed/playlist/37i9dQZF1DX2PQDq3PdrHQ?utm_source=generator&theme=0"
    # type='video', selected_url)="https://www.youtube.com/embed/JmEGknad17w"
    # list_url = DATA_PROVIDER.get_url(type, category)
    # print(list_url)
    # selected_url = select_random_from_list(list_url)
    # print(selected_url)
    return render_template("content_media.html", user_type=type, media_url=selected_url)


@app.route("/select_type", methods=['GET', 'POST'])
def content_selection_type():
    user_type = None
    form = TypeForm()

    # If there is a submit (aka POST of the form) the below checks will be executed.
    if form.validate_on_submit():
        if form.data["submit_sound"]:
            user_type = "sound"
            print(user_type)
        if form.data["submit_video"]:
            user_type = "video"
            print(user_type)
        return redirect(url_for("content_selection_category", type_p=user_type))

    # If no post method it will render the selection category html file
    return render_template("content_selection_type.html", form=form)


@app.route("/select_category", methods=['GET', 'POST'])
def content_selection_category():
    form = CategoryForm()
    user_category = "Victoria"
    user_type = request.args.get("type_p")
    print(user_type)
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
        return f'{user_type} {user_category}'
    # If no post method it will render the selection category html file
    return render_template("content_selection_category.html", form=form)


# @app.route("/media")
# def main_media():
#     form = TypeForm()
#     user_type = None
#     if form.validate_on_submit():
#         if form.data["submit_sound"]:
#             user_type = "sound"
#         if form.data["submit_video"]:
#             user_type = "video"
#         return render_template("content_selection_category.html", form=form)
#     return render_template("content_selection_type.html", form=form)


@app.route("/tips")
def tips():
    return render_template("tips.html")

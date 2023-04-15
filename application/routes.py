from flask import render_template, request, redirect, url_for
from application import app
from application.python_scripts.data_provider_service import DataProviderService
from application.forms.forms import TypeForm, CategoryForm, MediaOutputForm, AdminLandingForm, AdminLogin, \
    AdminUpdateUrl, AdminAddMedia, AdminDeleteMedia
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

    # If submit done (aka POST of the form) the below checks will be executed.
    # Each button has been set as a submit button, by clicking on the button, the user_type variable will be assigned
    # a string "sound" or "video
    if form.validate_on_submit():
        if form.data["submit_sound"]:
            user_type = "sound"
        if form.data["submit_video"]:
            user_type = "video"
        # redirect will execute the function inside the url_for(). User type selected on content_selection_type()
        # is being passed as a named parameter, so we can end up using it in the final screen content_media()
        return redirect(url_for("content_selection_category", type_p=user_type))

    # If no post method it will render the selection category html file
    return render_template("content_selection_type.html", form=form)


@app.route("/select_category", methods=['GET', 'POST'])
def content_selection_category():
    form = CategoryForm()  # instantiate form
    user_category = None  # empty variable to store the user's type selection
    user_type = request.args.get("type_p")  # named variable stored when select_type was rendered

    # If submit done (aka POST of the form) the below checks will be executed.
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
        # content_selection_type() and content_selection_category() will be passed as a named parameters, so we can
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


# @app.route("/admin_login")
# def admin_login():
#     return render_template("admin_login.html")


@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
    form = AdminLogin()  # instantiate form
    error = ""
    if request.method == 'POST':
        email = request.form['admin_email']
        password = request.form['admin_password']

        # checks validation of the inputted admin email and password
        sql = "SELECT * FROM admins WHERE admin_email = %s AND admin_password = %s AND admin_status = 'active'"
        DATA_PROVIDER.cursor.execute(sql, (email, password))
        result = DATA_PROVIDER.cursor.fetchone()

        if result is not None:
            # If the admin email and password are correct, go to the admin landing page
            return redirect(url_for("admin_landing"))
        else:
            # If the admin email and password are incorrect, display an error message
            error = "Invalid email or password"

    return render_template("admin_login.html", message=error, form=form)


@app.route("/admin_landing", methods=['GET', 'POST'])
def admin_landing():
    form = AdminLandingForm()  # instantiate form

    if form.validate_on_submit():
        # If user hits "Select another video/audio" it calls returns the function again
        if form.data["submit_add"]:
            return redirect(url_for("admin_add"))
        elif form.data["submit_update"]:
            return redirect(url_for("admin_update_url"))
        elif form.data["submit_delete"]:
            return redirect(url_for("admin_delete"))

    return render_template("admin_landing.html", form=form)


@app.route("/admin_update", methods=['GET', 'POST'])
def admin_update_url():
    form = AdminUpdateUrl()  # instantiate form
    msg = ""

    if request.method == 'POST':

        try:
            # Try block to check that both ID and URL have been provided
            media_id_toupdate = int(request.form['media_id'])
            media_url = request.form['media_url']

        except ValueError:
            # Except block to catch the Value Error when no data is provided
            msg = "Update not executed, provide an ID and URL."

        else:
            # Else block to execute whenever there is no errors (aka when both ID and URL have been provided)
            sql_idcheck = "SELECT media_id, media_url FROM media WHERE media_id=%s;"
            DATA_PROVIDER.cursor.execute(sql_idcheck, media_id_toupdate)
            result_idcheck = DATA_PROVIDER.cursor.fetchone()
            # print(result_idcheck)

            if result_idcheck[0] > 0:
                sql_updateurl = "UPDATE media SET media_Url=%s WHERE media_id=%s;"
                result_update = DATA_PROVIDER.cursor.execute(sql_updateurl, (media_url, media_id_toupdate))
                # conn.commit() is needed to execute the UPDATE. Without the commit() MySQL starts the transaction to
                # UPDATE but if no commit() is found, it will rollback directly
                # Ref link: https://stackoverflow.com/questions/17758074/pymysql-update-query
                DATA_PROVIDER.conn.commit()

                if result_update:
                    # print(f'result_update "{result_update}": {type(result_update)}')
                    # print(f'media_url "{media_url}": {type(media_url)}')
                    # print(f'media type "{media_id_toupdate}": {type(media_id_toupdate)}')
                    msg = "URL updated!"

                # print(f'result type "{result}": {type(result)}')
                # print(f'media type "{media_id}": {type(media_id)}')
            else:
                if not result_idcheck:
                    msg = "Unknown Media ID, update not executed."
                else:
                    msg = "Update not executed."
                # print(f'result type "{result}": {type(result)}')
                # print(f'media type "{media_id}": {type(media_id)}')

    return render_template("admin_updateurl.html", form=form, message=msg)


@app.route("/admin_add", methods=['GET', 'POST'])
def admin_add():
    form = AdminAddMedia()
    msg = ''
    sql_type = "SELECT DISTINCT type_id, type_name FROM type_media;"
    DATA_PROVIDER.cursor.execute(sql_type)
    result_type = DATA_PROVIDER.cursor.fetchall()
    print(result_type)
    msg_type = ''
    for type_tuple in result_type:
        msg_type += f'  {type_tuple[0]}: {type_tuple[1]}'
    return render_template("admin_add.html", form=form, message=msg, helper_type=msg_type)


@app.route("/admin_delete", methods=['GET', 'POST'])
def admin_delete():
    form = AdminDeleteMedia()
    msg = ''

    if request.method == 'POST':
        try:
            # Try block to check that media ID has been provided
            media_id = int(request.form['media_id'])
        except ValueError:
            # Except block to catch the Value Error when no data is provided
            msg = "Deletion not executed, provide a valid ID."
        else:
            # Else block to execute whenever there is no errors (aka when ID has been provided)
            sql_idcheck = "SELECT media_id FROM media WHERE media_id=%s;"
            DATA_PROVIDER.cursor.execute(sql_idcheck, media_id)
            result_idcheck = DATA_PROVIDER.cursor.fetchone()

            if result_idcheck:
                sql_delete = "DELETE FROM media WHERE media_id=%s;"
                result_delete = DATA_PROVIDER.cursor.execute(sql_delete, media_id)
                DATA_PROVIDER.conn.commit()

                if result_delete:
                    msg = "Media successfully deleted!"
            else:
                msg = "Media ID not found, deletion not executed."

    return render_template("admin_delete.html", form=form, message=msg)

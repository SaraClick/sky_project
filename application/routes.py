from flask import render_template, request
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


# @app.route("/admin_login")
# def admin_login():
#     return render_template("admin_login.html")


@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
    error = ""
    if request.method == 'POST':
        admin_email = request.form['admin_email']
        admin_password = request.form['admin_password']

        # checks validation of the inputted admin email and password
        sql = "SELECT * FROM admins WHERE admin_email = %s AND admin_password = %s AND admin_status = 'active'"
        DATA_PROVIDER.cursor.execute(sql, (admin_email, admin_password))
        result = DATA_PROVIDER.cursor.fetchone()

        if result is not None:
            # If the admin email and password are correct, go to the admin landing page
            return render_template('admin_landing.html')
        else:
            # If the admin email and password are incorrect, display an error message
            error = "Invalid email or password"

    return render_template("admin_login.html", title="Admin Login", message=error)


@app.route("/admin_landing")
def admin_landing():
    return render_template("admin_landing.html")

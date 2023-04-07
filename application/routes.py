from flask import render_template
from application import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# @app.route('/welcome/<name>/')
# def template_base(name):
#     return render_template('base.html', name=name, group='Everyone')

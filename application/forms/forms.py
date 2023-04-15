from wtforms import SubmitField, StringField
from flask_wtf import FlaskForm


# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm
class TypeForm(FlaskForm):
    # instantiating various input fields
    submit_sound = SubmitField("sound")
    submit_video = SubmitField("video")


class CategoryForm(FlaskForm):
    submit_ocean = SubmitField("ocean")
    submit_rain = SubmitField("rain")
    submit_whale = SubmitField("whale")
    submit_brown_noise = SubmitField("brown_noise")
    submit_white_noise = SubmitField("white_noise")
    submit_instrumental = SubmitField("instrumental")


class MediaOutputForm(FlaskForm):
    submit_new_media = SubmitField("new_media")


class AdminLogin(FlaskForm):
    admin_email = StringField("Email")
    admin_password = StringField("Password")
    submit_login = SubmitField("submit_login")


class AdminLandingForm(FlaskForm):
    submit_add = SubmitField("add_media")
    submit_update = SubmitField("update_media")
    submit_delete = SubmitField("delete_media")


class AdminUpdateUrl(FlaskForm):
    media_id = StringField("Email")
    media_url = StringField("Password")
    submit_update = SubmitField("submit_update")








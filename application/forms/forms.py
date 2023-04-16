from wtforms import SubmitField, StringField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


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
    media_id = StringField("media_id")
    media_url = StringField("media_url")
    submit_update = SubmitField("submit_update")


# Added dropdowns to help admins add media easier
class AdminAddMedia(FlaskForm):
    media_title = StringField("media_title")
    media_url = StringField("media_url")
    type_id = SelectField("Type", choices=[(1, "video"), (2, "sound")], validators=[InputRequired()], coerce=int)
    source_id = SelectField("Source", choices=[(1, "youtube"), (2, "spotify")], validators=[InputRequired()], coerce=int)
    category_id = SelectField("Category", choices=[(1, "brown noise"), (2, "white noise"), (3, "ocean"), (4, "whale"), (5, "rain"), (6, "instrumental")], validators=[InputRequired()], coerce=int)
    submit_add = SubmitField("submit_add")


class AdminDeleteMedia(FlaskForm):
    media_id = StringField("media_id")
    media_url = StringField("media_url")
    submit_delete = SubmitField("submit_delete")

from wtforms import SubmitField
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
    submit_favourite = SubmitField("favourite")










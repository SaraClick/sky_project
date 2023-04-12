from wtforms import SubmitField
from flask_wtf import FlaskForm


# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm
class TypeForm(FlaskForm):
    # instantiating various input fields
    submit_sound = SubmitField("Sound")
    submit_video = SubmitField("Video")

class CategoryForm(FlaskForm):
    pass


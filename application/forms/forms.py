from wtforms import SubmitField
from flask_wtf import FlaskForm


# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm
class SoundForm(FlaskForm):
    # instantiating various input fields
    submit_type = SubmitField("Sound")

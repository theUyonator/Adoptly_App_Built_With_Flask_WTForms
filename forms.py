from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange

class AddPetForm(FlaskForm):
    """This class handles the addition of Pets"""

    name = StringField("Pet Name",
                        validators=[InputRequired(message="Please Enter Pet Name")])

    species = SelectField("Species",
                        choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')])

    photo_url = StringField("Photo Url",
                            validators=[Optional(), URL()])

    age = IntegerField("Age",
                        validators=[Optional(), NumberRange(min=0, max=30)])

    sex = SelectField("Sex",
                choices=[("Male", "Male"), ("Female", "Female"), ("Non-Binary", "Non-Binary")],
                validators=[Optional()])

    notes = TextAreaField("Notes",
                        validators=[Optional(), Length(min=10, max=250, message="You exceeded the maximum characters allowed (250)")])

    available = BooleanField("is_available ?")


class EditPetForm(FlaskForm):
    """This class handles editing of existing pet information"""

    photo_url = StringField("Photo Url",
                            validators=[Optional(), URL()])


    notes = TextAreaField("Notes",
                        validators=[Optional(), Length(min=10, max=250, message="You exceeded the maximum characters allowed (250)")])


    available = BooleanField("is_available ?")
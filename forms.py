from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField,TextAreaField, BooleanField
from wtforms.validators import InputRequired, AnyOf, Optional, NumberRange, url

class AddPetForm(FlaskForm):
    name = StringField('Pet Name',
                       validators=[InputRequired()])
    species = StringField('Species',
                          validators=[InputRequired(), 
                                      AnyOf(values=["cat", "dog", "porcupine"],
                                            message="Must be a Cat, Dog, or Porcupine")])
    photo_url = URLField('Enter a Photo Url',
                         validators=[Optional(),
                                     url(message="Must be a valid URL")])
    age = IntegerField('Age',
                       validators=[Optional(),
                                   NumberRange(min=0,
                                               max=30,
                                               message="Only accepts up to 30 years old")])
    notes = TextAreaField('Notes')
    available = BooleanField('Is your Pet available for adoption?')
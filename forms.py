from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField,TextAreaField, BooleanField

class AddPetForm(FlaskForm):
    name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = URLField('Enter a Photo Url')
    age = IntegerField('Age')
    notes = TextAreaField('Notes')
    available = BooleanField('Is your Pet available for adoption?')
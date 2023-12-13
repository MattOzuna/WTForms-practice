from app import db,app
from models import Pet

with app.app_context():
    db.drop_all()
    db.create_all()

    new_pet = Pet(name='Copper',
                  species='Yellow Lab', 
                  age=7, 
                  photo_url='https://i.etsystatic.com/6226037/r/il/be2698/2006003775/il_1588xN.2006003775_kwvx.jpg',
                  notes='My first Dog', 
                  available=False)

    db.session.add(new_pet)
    db.session.commit()
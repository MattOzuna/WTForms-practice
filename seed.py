from app import db,app
from models import Pet

with app.app_context():
    db.drop_all()
    db.create_all()

    new_pet = Pet(name='Copper',
                  species='Dog', 
                  age=7, 
                  photo_url='https://i.etsystatic.com/6226037/r/il/be2698/2006003775/il_1588xN.2006003775_kwvx.jpg',
                  notes='My first Dog', 
                  available=False)
    
    new_pet2 = Pet(name='Madison',
                  species='Dog', 
                  age=7, 
                  photo_url='https://www.rvc.ac.uk/Media/Default/VetCompass/Chocolate%20Lab%20on%20Grass.jpg',
                  notes='My Second Dog', 
                  available=False)

    db.session.add_all([new_pet, new_pet2])
    db.session.commit()
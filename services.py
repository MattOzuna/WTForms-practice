from models import db, Pet

def addPetDataToDB(form):
    name=form.name.data
    species=form.species.data
    photo_url= form.photo_url.data if form.photo_url.data else None
    age=form.age.data
    notes=form.notes.data
    available=form.available.data

    new_pet=Pet(name=name,
                species=species,
                photo_url=photo_url, 
                age=age, notes=notes, 
                available=available)
    
    db.session.add(new_pet)
    db.session.commit()

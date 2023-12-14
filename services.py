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

def editPetData(form, pet):
    
    pet.name = form.name.data
    pet.species = form.species.data
    pet.photo_url = form.photo_url.data if form.photo_url.data else "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
    pet.age = form.age.data
    pet.notes = form.notes.data
    pet.available = form.available.data

    db.session.commit()

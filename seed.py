"""Seed file for adoptly_db"""

from models import db, Pet
from app import app

# Create all tables 
db.drop_all()
db.create_all()

# Empty table if it already isn't empty
Pet.query.delete()


# Add Pets 

Dragon = Pet(name="Dragon", species="porcupine", photo_url="https://media.eurekalert.org/multimedia_prod/pub/web/199705_web.jpg", age=11, sex = "Male",
             notes="Dragon just is so adorable, he was saved from a burning Forest in Kinshasa and brought to the land of the free where he is now in a cage.",
             available=True)

Roscoe = Pet(name="Roscoe", species="dog", photo_url="https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2016/06/21195710/German-Shepherd-Dog-laying-down-in-the-backyard.jpeg", age=6, sex = "Male",
             notes="Roscoe is a good boy, he was rescued from a a car accident and his parents went on to meet the lord, he is looking for a sweet family",
             available=True)

Sasha = Pet(name="Sasha", species="cat", photo_url="https://www.rd.com/wp-content/uploads/2019/05/American-shorthair-cat-scaled.jpg", age=1, sex = "Female",
            notes="Sasha is a pretty little cute thing, she is looking for parents that will adore and take care of her")


#Add and commit pets to db

db.session.add(Dragon)
db.session.add(Roscoe)
db.session.add(Sasha)

db.session.commit()
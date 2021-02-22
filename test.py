from unittest import TestCase

from app import app
from models import db, Pet

# We use a differnt db for testing so that our adoptly db isn't cluttered

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptly_test_db'
app.config['SQLALCHEMY_ECHO'] = False

# To  make flask errors real errors as opposed to HTML pages, set testing configuration to true

app.config['TESTING'] = True

# Don't show debug toolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

#Disable CSRF for testing
app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()

class  PetViewsTestCase(TestCase):
    """This class contains methods that test the view functions of the Pet class"""

    def setUp(self):
        """This method creates a demo pet before every test method runs"""

        # Delete all pets in the db
        Pet.query.delete() 

        pet=Pet(name="Skyla", species="cat", age=11, notes="Skyla is a great cat")
        db.session.add(pet)
        db.session.commit()

        self.pet_id = pet.id

    def tearDown(self):
        """Clean up fouled transaction"""

        db.session.rollback()

    def test_pet_edit_form(self):
        """This method tests that a form for pet edits is generated as expected when the route is requested"""

        with app.test_client() as client:
            resp = client.get(f"/{self.pet_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<form", html)

    def test_pet_edit(self):
        """This methods test to see if data is updated when new data is sent in a post request to the eit form route"""
        with app.test_client() as client:
            resp = client.post(
                f"/{self.pet_id}",
                data={"name": "Frank", "species": "porcupine", "age": 17, "notes": "Frank the real deal"},
                follow_redirects=True
            )
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Frank", html)

            pet = Pet.query.get(self.pet_id)
            self.assertEquals(pet.name,"Frank")
            self.assertEquals(pet.species, "porcupine")

    def test_pet_edit_form_fail(self):
        """This method tests to see if the edit fails as expected when something that is not a url is entered """

        with app.test_client() as client:
            resp = client.post(
                f"/{self.pet_id}",
                data={"name": "Frank", "species": "porcupine", "age": 17, "photo_url": "cllsksll"},
                follow_redirects=True
            )

            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertNotIn("Frank", html)




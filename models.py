"""Models for aboptly-db"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to the Adoptly db"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """This model holds information on the structure of the pets table in the Adoptly_db"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    name = db.Column(db.Text,
                     nullable=False)
    
    species = db.Column(db.Text,
                        nullable=False)

    photo_url = db.Column(db.Text,
                        nullable=True,
                        default="https://nicolasmelis.com/wp-content/themes/panama/assets/img/empty/600x600.png")

    age = db.Column(db.Integer,
                    nullable=True)

    sex = db.Column(db.Text,
                    nullable=True)
    
    notes = db.Column(db.String(250),
                      nullable=True)

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)


    def __repr__(self):
        """This is a representation of the particular instance of the Pet class"""
        if self.age and self.sex:
            return f"<name = {self.name}, species = {self.species}, age = {self.age}, sex = {self.sex}, available = {self.available}>"

        return f"<name = {self.name}, species = {self.species}, available = {self.available}>"




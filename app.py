"""Adoptly Application"""


from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "aboptlypets"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Adoptly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)


####################### User Routes ################################

@app.route("/")
def homepage():
    """This view function renders the homepage for the adoptly app"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)

@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND PAGE"""

    return render_template('404.html'), 404

@app.route("/about/adoptly")
def about_adoptly():
    """This view function renders a page with information on Adoptly"""

    return render_template("about_us.html")

@app.route("/add", methods=["GET", "POST"])
def add_pets():
    """This view function renders the add pets form and handles the post request once the form is submitted"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        sex = form.sex.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, sex=sex, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} to the db")

        return redirect("/")

    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/pets/<int:pet_id>")
def show_pet_details(pet_id):
    """This view function renders the details of a particular pet"""

    pet = Pet.query.get_or_404(pet_id)

    return render_template("pet_details.html", pet=pet)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet_details(pet_id):
    """"This view function renders and submits a form that edits pet details in the Adoptly db"""

    pet=Pet.query.get_or_404(pet_id)
    form=EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet_id} updated!")
        return redirect(f"/pets/{pet.id}")
    else:
        return render_template("pet_edit_form.html", form=form, pet_id=pet_id)
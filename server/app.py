from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SKEY')

db = SQLAlchemy(app)

class NamePryze(FlaskForm):
    first_name = StringField('First Name')
    submit = SubmitField('submit')

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    noise = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    ticket = requests.get('http://ticket_api:5000/get_ticket')

    animal = requests.get('http://animal_noises_api:5000/get_animal') 
    noise = requests.post('http://animal_noises_api:5000/get_noise', data=animal.text) 

    last_five_animals = Animals.query.order_by(desc(Animals.id)).limit(5).all()
    db.session.add(
        Animals(
            type = animal.text,
            noise = noise.text
        )
    )
    db.session.commit()
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':

        if len(first_name) == 0: 
            error = "Please supply a first name No numbers No special-characters"

    return render_template('index.html', ticket=ticket.text, form=form, message=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
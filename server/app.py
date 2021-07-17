from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import requests
from os import getenv
import os 
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

class Raffle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)

class UserCheck:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = 'Please choose another first name' 
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

class SpecialCheck:
    def __init__(self, special, message=None):
        self.special = special
        if not message:
            message = 'No special characters'
        self.message = message 
    
    def __call__(self, form, field):
        firstname = field.data.lower()
        for character in firstname:
            if character in self.special:
                raise ValidationError(self.message)

class myForm(FlaskForm):
    firstname = StringField('First name', validators=[
        DataRequired(),
        UserCheck(message="Cant use this first name",banned = ['root','admin','sys']),
        Length(min=2,max=15),
        SpecialCheck(special=['!','?','*','"','£','$','%','^','&'])
        ])
    submit = SubmitField('Submit')
    
    def validate_firstname(self,firstname):
        for character in firstname.data:
            if character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                raise ValidationError('No numbers allowed')

@app.route('/', methods=['GET', 'POST'])
def home():

    form = myForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        if request.method == 'POST':
            ticket = requests.get('http://pryze_ticket_api:5000/get_ticket')
            brand = requests.post('http://pryze_class_api:5000/get_class', data=firstname)
            model = requests.post('http://pryze_prize_api:5000/get_prize', data=brand.text)
            
            last_five_entries = Raffle.query.order_by(desc(Raffle.id)).limit(5).all()
            db.session.add(
                Raffle(
                    ticket = ticket.text,
                    brand = brand.text,
                    model = model.text
                )
            )
            db.session.commit()

            return render_template('index.html', form = form, firstname=firstname, ticket=ticket.text, brand=brand.text, model=model.text, last_five_entries=last_five_entries)
    else:
        return render_template('index.html', form = form, firstname="", ticket="", brand="", model="")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
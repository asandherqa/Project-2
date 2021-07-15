from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import requests
import os
# from sqlalchemy import desc

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# db = SQLAlchemy(app)

class UserCheck:
    def __init__(self, banned, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.
        self.banned = banned
        if not message:
            message = 'Please choose another first name' # If no message chosen, then this default message is returned.
        self.message = message

    def __call__(self, form, field):
    # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.
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
        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.
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
    ticket = requests.get('http://pryze_ticket_api:5000/get_ticket')
    classserver = requests.post('http://pryze_class_api:5000/get_class', data=)

    form = myForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        return render_template('index.html', form = form, firstname=firstname, ticket=ticket.text, classserver=classserver.text)
    else:
        return render_template('index.html', form = form, firstname="", ticket=ticket.text, classserver=classserver.text)

@app.route('/firstname', methods=['POST'])
def firstname():
    form = myForm()
    firstnameserver = form.firstname.data
    return firstnameserver[request.data.decode('utf-8')]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import requests
import os
# from sqlalchemy import desc

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# db = SQLAlchemy(app)

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    ticket = requests.get('http://pryze_ticket_api:5000/get_ticket')
    
    error = ""

    form = BasicForm()
    if request.method == 'POST':
        first_name = form.first_name.data
        # for character in first_name:
        #         if character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        #            error = "No numbers allowed"
        # for character in first_name:
        #         if character in ['!','?','*','"','£','$','%','^','&']:
        #             error = "No special characters allowed"
        if len(first_name) == 0:
            error = "Please enter a first name"
        elif len(first_name) > 20:
            error = "Maximum characters is 20"
        elif character in ['!','?','*','"','£','$','%','^','&'] == character in first_name:
            error = "No special characters allowed"
        elif character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] == character in first_name:
            error = "No numbers allowed"
        else:
            error = "See pryze below"

    return render_template('index.html', form=form, message=error, ticket=ticket.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
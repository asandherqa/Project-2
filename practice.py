import random

def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':

        if len(first_name) == 0: 
            error = "Please supply a first name (No numbers or special-characters)"
        else:
            return "See pryze below"



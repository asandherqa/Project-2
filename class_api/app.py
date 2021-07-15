from flask import Flask
import random

app = Flask(__name__)

def get_class():
    
    class_first_name = 'aaron'

    class1 = ['Ferrari', 'Lamborghini', 'Aston Martin', 'McLaren', 'Bentley', 'Porsche']
    class2 = ['Candle', 'Toaster', 'Golf Clubs', 'Speaker', 'Headphones', 'Book']

    if 1 < len(class_first_name) <= 5:
        return class1
    elif 20 > len(class_first_name) > 6:
        return class2
    else:
        return 'No Pryze'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, request
import random
import requests

app = Flask(__name__)

@app.route('/get_prize', methods = ['POST'])
def get_class():

    brands = request.data.decode('utf-8')
    if brands == 'Ferrari':
        return random.choice(['488', 'Roma', '812'])
    elif brands == 'Lamborghini':
        return random.choice(['Aventador', 'Huracan', 'Urus'])
    elif brands == 'McLaren':
        return random.choice(['720S', 'Senna', '570S'])
    elif brands == 'Rolex':
        return random.choice(['Day-Date', 'Datejust', 'Sky Dweller'])
    elif brands == 'Audemars Piguet':
        return random.choice(['Millenary', 'Royal Oak', 'Code 11.59'])
    elif brands == 'Richard Mille':
        return random.choice(['74-02', '74-01', '72-01'])
    else:
        return 'No model error'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, request
import random
import requests

app = Flask(__name__)

@app.route('/get_class', methods = ['GET', 'POST'])
def get_class():

    # firstnameclass = requests.get('http://pryze_server:5000/firstname')
    # firstnameclass = firstnameclass.text
    classname = request.data.decode('utf-8')

    car = random.choice(['Ferrari', 'Lamborghini', 'McLaren'])
    watch = random.choice(['Rolex', 'Audemars Piguet', 'Richard Mille'])

    if len(classname) < 5:
        return car
    else:
        return watch

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
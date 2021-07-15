from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_class', methods = ['GET', 'POST'])
def get_class():

    firstnameclass = requests.post('http://pryze_server:5000/firstname')
    return firstnameclass

    # class1 = ["Ferrari", "Lamborghini", "Aston Martin", "McLaren", "Bentley", "Porche"]
    # class2 = ["Candle", "Toaster", "Golf Clubs", "Speaker", "Headphones", "Book"]

    # if 1 < len(firstnameclass) <= 5:
    #     return class1[request.data.decode('utf-8')]
    # else:
    #     return class2[request.data.decode('utf-8')]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
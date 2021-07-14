from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_ticket', methods = ['GET'])
def get_ticket():
    length = 5
    ticketx = []
    while len(ticketx) < length:
        num = random.randint(0, 9)
        ticketx.append(num)
    tickets = ''.join(map(str, ticketx))
    return tickets

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
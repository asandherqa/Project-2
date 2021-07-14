import random

def get_ticket():
    length = 5
    ticketx = []
    while len(ticketx) < length:
        num = random.randint(0, 9)
        ticketx.append(num)
    ticket = ''.join(map(str, ticketx))
    return ticket

print(get_ticket())


import random

import game
from math import sin, cos, sqrt, atan2, radians


def getRandom():
    return random.randint(1000000, 9999999)

def generateCity():
    return game.City("Cracov", "Poland", 100, 100)

def distance(x1, y1, x2, y2):
    R = 6373.0

    lat1 = radians(x1)
    lon1 = radians(y1)
    lat2 = radians(x2)
    lon2 = radians(y2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
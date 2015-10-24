import random
import db

import player
from math import sin, cos, sqrt, atan2, radians


def getRandom():
    return random.randint(1000000, 9999999)

def generateCity():
    name, country, x, y = db.getRandomCity(random.randint(1, 10000))
    return player.City(name, country, x, y)

def distance(x1, y1, x2, y2):
    R = 6373.0

    lat1 = radians(float(x1))
    lon1 = radians(float(y1))
    lat2 = radians(float(x2))
    lon2 = radians(float(y2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

def calculatePoints(dist, time):
    # return 10000 / dist**(1.0/2) * max(10-time, 0)  ## type 1
    return 10000 / dist**(13.0/17.0) * max(10-time, 0)**(4.0/5)
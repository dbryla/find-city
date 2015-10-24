import random
import game

def getRandom():
    return random.randint(1000000, 9999999)

def generateCity():
    return str(game.City("Cracov", "Poland", 100, 100))
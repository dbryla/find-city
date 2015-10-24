import os
import csv
import sqlite3

DB_PATH = os.path.join(os.path.join(os.path.dirname(__file__), "db"), 'cities.db')

def createDB():
    db_exists = False
    if os.path.isfile(DB_PATH):
        db_exists = True
        print "database exists"
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    if not db_exists:
        print "creating database"
        try:
            cursor.execute("CREATE TABLE Cities (id INTEGER PRIMARY KEY, "
                                                "country VARCHAR(255), "
                                                "name VARCHAR(255), "
                                                "latitude VARCHAR(255), "
                                                "longitude VARCHAR(255))")
            cursor.execute("CREATE TABLE Rank (id INTEGER PRIMARY KEY, "
                                                "name VARCHAR(255), "
                                                "points VARCHAR(255))")
            with open(os.path.join(os.path.join(os.path.dirname(__file__), "db"), '10000.txt'), 'rb') as csvfile:
                cities = csv.reader(csvfile)
                query = 'INSERT INTO Cities (country, name, latitude, longitude) VALUES (\"{}\", \"{}\", \"{}\", \"{}\")'
                for row in cities:
                    cursor.execute(query.format(row[0], row[1], row[2], row[3]))
            connection.commit()
        except Exception:
            print "error"
            raise
    connection.close()

def getRandomCity(index):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT name, country, latitude, longitude FROM Cities WHERE id = {}".format(index))
        row = cursor.fetchone()
        connection.close()
        return row[0], row[1], row[2], row[3]
    except Exception:
        raise

def isNewRecord(result):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT points FROM Rank WHERE points > {}".format(result))
        rows = cursor.fetchall()
        connection.close()
        if len(rows) < 10:
            return True
        return False
    except Exception:
        raise

def saveRecord(name, record):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    query = 'INSERT INTO Rank (name, points) VALUES (\"{}\", \"{}\")'
    cursor.execute(query.format(name, record))
    connection.commit()
    connection.close()

def readRecords():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT name, points FROM Rank ORDER BY points DESC LIMIT 10")
    return cursor.fetchall()

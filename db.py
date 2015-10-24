import os
import csv
import sqlite3

def createDB():
    db_path = os.path.join(os.path.join(os.path.dirname(__file__), "db"), 'cities.db')
    db_exists = False
    if os.path.isfile(db_path):
        db_exists = True
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    if not db_exists:
        try:
            cursor.execute("CREATE TABLE Cities (id INTEGER PRIMARY KEY, "
                                                "country VARCHAR(255), "
                                                "name VARCHAR(255), "
                                                "latitude VARCHAR(255), "
                                                "longitude VARCHAR(255))")
            with open(os.path.join(os.path.join(os.path.dirname(__file__), "db"), '10000.txt'), 'rb') as csvfile:
                cities = csv.reader(csvfile)
                query = 'INSERT INTO Cities (country, name, latitude, longitude) VALUES (\"{}\", \"{}\", \"{}\", \"{}\")'
                for row in cities:
                    cursor.execute(query.format(row[0], row[1], row[2], row[3]))
            connection.commit()
        except Exception:
                raise
    connection.close()
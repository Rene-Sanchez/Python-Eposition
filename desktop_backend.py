import sqlite3
import pandas

def create_table():
    connect = sqlite3.connect("Horse_Ranches.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ranch (id INTEGER PRIMARY KEY, name TEXT, address TEXT, rating TEXT, phone TEXT, website TEXT, notes TEXT)")
    connect.commit()
    connect.close()

def insert(name,address,rating,phone,website,notes):
    connect = sqlite3.connect("Horse_Ranches.db")
    cursor = connect.cursor()
    connect.execute("INSERT INTO ranch VALUES (NULL,?,?,?,?,?,?)",(name,address,rating,phone,website,notes))
    connect.commit()
    connect.close()

def view():
    connect = sqlite3.connect("Horse_Ranches.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM ranch")
    rows = cursor.fetchall()
    connect.close()
    return rows

def search(name="",address="",rating=""):
    name= name.title()
    address=address.title()
    address = '%'+address+'%'
    name = '%'+name+'%'
    rating = '%'+rating+'%'
    connect = sqlite3.connect("Horse_Ranches.db")
    cursor = connect.cursor()
    if address != "%%":
        cursor.execute("SELECT * FROM ranch WHERE address LIKE ? ", (address,))
    elif rating != "%%":
        cursor.execute("SELECT * FROM ranch WHERE rating LIKE ? ", (rating,))
    elif name != "%%":
        cursor.execute("SELECT * FROM ranch WHERE name LIKE ? ", (name,))
    else:
        None
    rows = cursor.fetchall()
    connect.close()
    return rows

def delete(id):
    connect = sqlite3.connect("Horse_Ranches.db")
    cursor = connect.cursor()
    connect.execute("DELETE FROM ranch WHERE id=?",(id,))
    connect.commit()
    connect.close()

def update(id,name,address,rating,phone,website,notes):
    connect = sqlite3.connect("Horse_Ranches.db")
    cursor = connect.cursor()
    connect.execute("UPDATE ranch SET name=?, address=?,rating=?,phone=?, website=?, notes=? WHERE id=?", (name,address,rating,phone,website,notes,id))
    connect.commit()
    connect.close()

import googlemaps
import pygmaps

def mapping(item):
    gmaps= googlemaps.Client(key='AIzaSyC0Mmo-RKU6ZhYVuEbjOBnBBqkOjd9Ju_8')
    gmap = pygmaps.maps(34.213320, -118.457529, 12)
    geocode = gmaps.geocode(item)[0]
    latlong = geocode['geometry']['location']
    gmap.addpoint(latlong['lat'],latlong['lng'],)
    gmap.draw("map.html")

create_table()
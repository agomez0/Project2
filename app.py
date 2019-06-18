import os

from datetime import datetime

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import mysqlinfo

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# Database Setup
#################################################

# crimes_db database in mysql
dbname = "crimes_db"

# connection to mysql
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{mysqlinfo['username']}:{mysqlinfo['password']}@{mysqlinfo['host']}:{mysqlinfo['port']}/{dbname}"

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
venues = Base.classes.venues
crimes = Base.classes.crimes_updated

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    
@app.route("/map_index.html")
def map_index():
    """Return the heat map."""
    return render_template("map_index.html")

@app.route("/line_index.html")
def line_index():
    """Return the line plot."""
    return render_template("line_index.html")

@app.route("/table_index.html")
def table_index():
    """Return the table."""
    return render_template("table_index.html")

#obtains the coordinates of the arenas
#Appends a dictionary of information for each coordinate to a list
@app.route("/venue_coords")
def venue_coords():

    results = db.session.query(venues.latitude, venues.longitude, venues.venue).all()
    coords_list = []
    for result in results:
        coords = {}
        coords["latitude"] = result[0]
        coords["longitude"] = result[1]
        coords["venue"] = result[2]
        coords_list.append(coords)

    return jsonify(coords_list)

#obtains the coordinates of the crimes
@app.route("/crime_coords")
def crime_coords():
    sel = [
        crimes.latitude,
        crimes.longitude
    ]
    results = db.session.query(*sel).all()

    return jsonify(results)

#obtains information about the crimes near Staples Center
#Appends a dictionary of information for each crime to a list
@app.route("/staples_crimes")
def staples_crimes():
    sel = [
        crimes.date_occurred,
        crimes.time_occurred,
        crimes.dist_from_staples_center
    ]

    results = db.session.query(*sel).filter(crimes.dist_from_staples_center <= 1.5).order_by(crimes.dist_from_staples_center.asc()).all()

    staples_list = []
    for result in results:
        staples_crime = {}
        staples_crime["date_occurred"] = result[0].strftime("%m/%d/%Y")
        staples_crime["time_occurred"] = result[1].strftime("%H:%M:%S")
        staples_crime["dist_from_venue"] = result[2]
        staples_list.append(staples_crime)

    return jsonify(staples_list)

#obtains information about the crimes near the Coliseum
#Appends a dictionary of information for each crime to a list
@app.route("/coliseum_crimes")
def coliseum_crimes():
    sel = [
        crimes.date_occurred,
        crimes.time_occurred,
        crimes.dist_from_coliseum
    ]

    results = db.session.query(*sel).filter(crimes.dist_from_coliseum <= 1.5).order_by(crimes.dist_from_coliseum.asc()).all()

    coliseum_list = []
    for result in results:
        coliseum_crime = {}
        coliseum_crime["date_occurred"] = result[0].strftime("%m/%d/%Y")
        coliseum_crime["time_occurred"] = result[1].strftime("%H:%M:%S")
        coliseum_crime["dist_from_venue"] = result[2]
        coliseum_list.append(coliseum_crime)

    return jsonify(coliseum_list)

#obtains information about the crimes near Dodger Stadium
#Appends a dictionary of information for each crime to a list
@app.route("/dodger_crimes")
def dodger_crimes():
    sel = [
        crimes.date_occurred,
        crimes.time_occurred,
        crimes.dist_from_dodger_stadium
    ]

    results = db.session.query(*sel).filter(crimes.dist_from_dodger_stadium <= 1.5).order_by(crimes.dist_from_dodger_stadium.asc()).all()

    dodger_list = []
    for result in results:
        dodger_crime = {}
        dodger_crime["date_occurred"] = result[0].strftime("%m/%d/%Y")
        dodger_crime["time_occurred"] = result[1].strftime("%H:%M:%S")
        dodger_crime["dist_from_venue"] = result[2]
        dodger_list.append(dodger_crime)

    return jsonify(dodger_list)

#Obtains information about all the crimes; will be used for the dynamic table
#Appends a dictionary of information for each crime to a list
@app.route("/table")
def table():
    sel = [
        crimes.date_occurred,
        crimes.time_occurred,
        crimes.area_name,
        crimes.crime_description,
        crimes.dist_from_staples_center,
        crimes.dist_from_coliseum,
        crimes.dist_from_dodger_stadium
    ]

    results = db.session.query(*sel).all()

    table_list = []
    for result in results:
        table_values = {}
        table_values["date"] = result[0].strftime("%m/%d/%Y")
        table_values["time"] = result[1].strftime("%H:%M:%S")
        table_values["area"] = result[2]
        table_values["description"] = result[3]
        table_values["staplesdist"] = str(result[4])
        table_values["coliseumdist"] = str(result[5])
        table_values["dodgerdist"] = str(result[6])
        table_list.append(table_values)

    return jsonify(table_list)

if __name__ == "__main__":
    app.run()
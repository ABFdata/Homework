# import dependencies 
import pandas as pd
import numpy as np
import warnings

# sqlalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

# flask 
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# assign measurement and station classes to variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session
# a session means that you want to do something to your data
session = Session(engine)

# flask set up
app = Flask(__name__)

# flask routes
@app.route("/")
def main():
    """List all available api routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation<br/>"
        f"/api/v1.0/stations - Stations<br/>"
        f"/api/v1.0/tobs - Temperature Observation<br/>"
        f"/api/v1.0/temperature - Temperature Start<br/>"
        f"/api/v1.0/start</br>"
        f"/api/v1.0/start/tmin</br>"
        f"/api/v1.0/start/tavg</br>"
        f"/api/v1.0/start/tmax")

# prcp route
@app.route("/api/v1.0/precipitation")
def precipitation_test1():
    """Return a list of dates and tobs"""
    # Query for the dates and prcp from last year
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date <= '2017-08-23').\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date.desc()).all()
    
    # Convert list of tuples into normal list
    prcp_list = list(np.ravel(results))
    
    return jsonify(prcp_list)

# stations route
@app.route("/api/v1.0/stations")
def stations_test1():
    """Return a json list of stations from the dataset"""
    # Query stations
    station_results = session.query(Measurement.station, func.count(Measurement.station).label("most_active_stations"))\
    .group_by(Measurement.station).order_by("most_active_stations DESC").all()
    
    station_results_list = list(np.ravel(station_results))
    
    return jsonify(station_results_list)

# tobs route
@app.route("/api/v1.0/tobs")
def tobs_test1():
    """Return a json list of tobs for the previous year"""
    # Query tobs
    tobs_results = session.query(Measurement.station, Measurement.tobs, func.count(Measurement.tobs).\
    label("highest_observations")).\
    group_by(Measurement.tobs).\
    filter(Measurement.date <= '2017-08-23').\
    filter(Measurement.date >= '2016-08-23').\
    order_by("highest_observations DESC").all() 
    
    tobs_results_list = list(np.ravel(tobs_results))
    
    return jsonify(tobs_results_list)   

# min, avg, max tobs route
# max temp for given start-end range
@app.route("/api/v1.0/temperature")
def temps_test1():
    """Return a json list of temps for a given start or start-end range."""
    # Query  temps
    temps_results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date <= '2017-08-22').\
    filter(Measurement.date >= '2017-08-17').\
    order_by(Measurement.tobs.desc()).all() 

    temps_results_list = list(np.ravel(temps_results))
    
    return jsonify(temps_results_list)

# tmin 
@app.route("/api/v1.0/start")
@app.route("/api/v1.0/start/tmin")
def temps_start_test1():
    """Returns tmin"""
    min_temps_results = session.query(func.min(Measurement.tobs)).filter(Measurement.date <= '2017-08-22').\
    filter(Measurement.date >= '2017-08-17').\
    order_by(Measurement.date.desc()).all()
    
    min_temps_results_list = list(np.ravel(min_temps_results))
    
    return jsonify(min_temps_results_list)

# tavg
@app.route("/api/v1.0/start")
@app.route("/api/v1.0/start/tavg")
def temps_start_tavg1():
    """returns tavg"""
    avg_temps_results = session.query(func.avg(Measurement.tobs)).filter(Measurement.date <= '2017-08-22').\
    filter(Measurement.date >= '2017-08-17').\
    order_by(Measurement.date.desc()).all()
    
    avg_temps_results_list = list(np.ravel(avg_temps_results))
    
    return jsonify(avg_temps_results_list)

# tmax
@app.route("/api/v1.0/start")
@app.route("/api/v1.0/start/tmax")
def temps_start_tmax1():
    """returns tmax"""
    max_temps_results = session.query(func.max(Measurement.tobs)).filter(Measurement.date <= '2017-08-22').\
    filter(Measurement.date >= '2017-08-17').\
    order_by(Measurement.date.desc()).all()
    
    max_temps_results_list = list(np.ravel(max_temps_results))
    
    return jsonify(max_temps_results_list)

if __name__ == '__main__':
    app.run()



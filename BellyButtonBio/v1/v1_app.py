# import dependencies
import pandas as pd
import numpy as np 
import warnings

# import sqlalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy import func 
from sqlalchemy import inspect

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, Numeric

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

# flask dependencies
from flask import Flask, jsonify, render_template

# database set up
engine = create_engine("sqlite:///bbb.sqlite")
conn = engine.connect()

# refelct an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# assign classes to variables
sample_names = Base.classes.samples
otu_des = Base.classes.otu
sample_meta = Base.classes.samples_metadata

# create a session
# session means that you want to do something to your data
session = Session(engine)

# use inspector to inspect engine
inspector = inspect(engine)

# get col names for samples table
# this stores a col info as a tuple within a list
sample_name_col = inspector.get_columns('samples')

# slice out "name" in sample_name_col
sample_names_list = [item["name"] for item in sample_name_col]
del sample_names_list[0]

# use pandas to read Belly_Button_Biodiversity_Metadata.csv
bbb_meta_df = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')

# create new df from bbb_meta_df with the following columns:
# AGE, BBTYPE, ETHNICITY, GENDER, LOCATION, SAMPLEID
bbb_meta_clean = bbb_meta_df[['AGE', 'BBTYPE', 'ETHNICITY','GENDER', 'LOCATION', 'SAMPLEID']]

# convert bbb_meta_clean to a dictionary
bbb_meta_dict = bbb_meta_clean.to_dict(orient='records')

# returns an integer value for the weekly washing frequency 'WFREQ'
freq_df = bbb_meta_df[['SAMPLEID', 'WFREQ']]

# create new object with just SAMPLEID col
samplid = freq_df['SAMPLEID'].tolist()

# create an empty to store the concat BB + samplid
s_format = []
# loop through list and append
for i in range(len(samplid)):
    s_format.append('BB_' + str(samplid[i]))

# takes the WFREQ col and turns it into a list
wfreq = freq_df['WFREQ'].tolist()

# read in otu csv
otu_df1 = pd.read_csv('belly_button_biodiversity_otu_id.csv',dtype=object)

# sort otu_df1 to DESC values
otu_df1_sort = otu_df1.sort_values('otu_id', ascending=False)

# sort out otu from otu_df1
otu_df = otu_df1_sort[['otu_id']]

# sets otu_id in otu_df to a new list called value
# we will add this list to our dictionary - sample_dict
value = otu_df['otu_id'].tolist()

# this strips the quotes from value
value = list(map(int, value))

# sorts the SAMPLE ID column from bbb_meta_df
sample_sort = bbb_meta_df.sort_values('SAMPLEID', ascending=False)

# creates a descending list of SAMPLEID
sample_value = sample_sort['SAMPLEID'].tolist()

# dictionary {otu_ids: [1,2,3]}
# the above is the kind of dictionary we want to make
sample_dict = {'otu_ids': value, 'sample_values': sample_value}

# flask set up
app = Flask(__name__, static_folder="static")

# app routes

# first route returns to the dashboard home page
@app.route("/")
def index():
    return render_template("index.html")

# # second route returns a list of sample names
@app.route("/names")
def names():
    """Return list of sample names"""
    sample_names_list

    return jsonify(sample_names_list)


# third route returns a list of OTU descriptions
@app.route("/otu")
def otu_func():
    """List of OTU descriptions."""
    otu_results = session.query(otu_des.lowest_taxonomic_unit_found).all()
    otu_results_list = list(np.ravel(otu_results))

    return jsonify(otu_results_list)

# fourth route returns a json dictionary of sample metadata
@app.route("/metadata")
def meta_func():
    """MetaData for a given sample."""

    bbb_meta_dict

    return jsonify(bbb_meta_dict)



# fifth route returns an integer value for the weekly washing frequency 'WFREQ'
@app.route('/freq')
def freq_func():
    wfreq
    #s_format 
    return jsonify(wfreq)
    #return jsonify(s_format)

# sixth route reutrns a list of dictionaries containing sorted lists for otu_ids and sample_values
@app.route('/samples')
def d_func():
    
    sample_dict
    
    return jsonify(sample_dict)



if __name__ == "__main__":
    app.run(debug=True)

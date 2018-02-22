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

# flask set up
app = Flask(__name__, static_folder="static")

# app routes

# first route returns to the dashboard home page
@app.route("/")
def index():
    # return render_template("index.html")
    return render_template("index.html", sample_names_list=sample_names_list)
    return render_template("index_html", otu_results_list=otu_results_list)
    return render_template("index_html", bbb_meta_dict=bbb_meta_dict)
    return render_template("index_html", wfreq=wfreq)
    return render_template("index_html", sample_dict=sample_dict)


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
@app.route('/metadata/<sample>')
# here we have to def a func for <sample>
def show_meta_sample(sample = 'BB_940'):
    # return 'Metadata %s' % sample
    # bbb_meta_dict
    # return jsonify(bbb_meta_dict)

    # sets index to SAMPLEID
    bbb_meta_clean2 = bbb_meta_clean.set_index('SAMPLEID')

    # create a variable sample and set it to 940
    # sample = 'sample'

    # strip BB_ from sample
    sampleID = int(sample.replace('BB_', ""))

    # create a new object and use loc
    bbb_ID = bbb_meta_clean2.loc[sampleID]

    #  set SAMPLEID = sampleID
    bbb_ID['SAMPLEID'] = sampleID

    # results 
    results = bbb_ID[["AGE","BBTYPE","ETHNICITY","GENDER","LOCATION",
    "SAMPLEID"]]

    # results to dict
    meta_dict = results.to_dict()
    return jsonify(meta_dict)



# fifth route returns an integer value for the weekly washing frequency 'WFREQ'
# @app.route('/freq')
@app.route('/wfreq/<samplewf>')
def show_freq_sample(samplewf = 'BB_940'):

    # set index to sample id and store in wf
    wf = bbb_meta_df.set_index('SAMPLEID')

    # samplewf = 'BB_940'

    # strip BB_ 
    samplewf_ID = int(samplewf.replace("BB_",""))

    # create a new df object and use .loc
    wf_new = wf.loc[[samplewf_ID],['WFREQ']]

    # get the int value of WFREQ
    results2 = wf_new["WFREQ"].item()

    return jsonify(results2)
    
# sixth route reutrns a list of dictionaries containing sorted lists for otu_ids and sample_values
@app.route('/samples/<sample>')
def show_samp(sample= 'BB_943'):

    # read in samples csv
    bbb_samplesDF = pd.read_csv('belly_button_biodiversity_samples.csv')

    # create a new df object that filters sample & otu_id
    bbb_samplesDF_filter = bbb_samplesDF.filter(items = [sample, 'otu_id'])

    # create a new object to sort filtered DF by DESC
    bbb_samplesDF_filter_sort = bbb_samplesDF_filter.sort_values(by=sample, ascending=False)

    # create df object to sort > 0
    bbb_sampleDF_nan1 = bbb_samplesDF_filter_sort[bbb_samplesDF_filter_sort > 0]
   
    # drops null
    bbb_sampleDF_nan2 = bbb_sampleDF_nan1.dropna()

    # this takes the sample col or the SAMPLEID col and stores it into a list
    sample_val = bbb_sampleDF_nan2[sample].tolist()

    # stores the otu_id col into a list
    otu_ids = bbb_sampleDF_nan2['otu_id'].tolist()

    # create a dictionary stored in a list
    otu_samp_dict = [{'otu_ids': otu_ids, 'sample_values': sample_val}]

    return jsonify (otu_samp_dict)




if __name__ == "__main__":
    app.run(debug=True)

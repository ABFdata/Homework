# import dependencies
import pandas as pd    

from flask import Flask, jsonify, render_template
app = Flask(__name__, static_folder="static")

# app routes

# first route returns to the dashboard home page
@app.route("/")
def index():
    return render_template("index.html")

# # second route returns a list of sample names
# @app.route("/names")

# # third route returns a list of OTU descriptions
# @app.route("/otu")

# # fourth route returns a json dictionary of sample metadata
# @app.route("/metadata/<sample>")

# # fifth route returns an integer value for the weekly washing frequency 'WFREQ'
# @app.route('w/freq/<sample>')

if __name__ == "__main__":
    app.run(debug=True)

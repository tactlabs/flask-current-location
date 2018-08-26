from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
from flask_googlemaps import GoogleMaps

from flask_googlemaps import Map


app = Flask(__name__)

GoogleMaps(app, key="AIzaSyAPIdlhi7Xzv8uvrDDnxhiwttiyjLle6DQ")

@app.route('/')
def home():
    mymap = Map(

                identifier="view-side",

                varname="mymap",

                style="height:720px;width:1100px;margin:0;", # hardcoded!

                lat=37.4419, # hardcoded!

                lng=-122.1419, # hardcoded!

                zoom=15,

                markers=[(37.4419, -122.1419)] # hardcoded!

            )

    return render_template('example.html', mymap=mymap)

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
    
    Get Current Location:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
'''
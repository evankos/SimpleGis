# Simple Flask Rest Gis App 

This is [Flask](http://flask.pocoo.org/) app that expects a POST request
at "/api/v1.0/population" of 'Content-Type': 'application/json' and matching 
the pattern: {     "longitude": 39.122229,     "latitude": -77.133578,     "radius": 30   }.

Only data for the US is available.

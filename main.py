# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

# [START imports]
from flask import Flask, request, abort, jsonify
from uszipcode import ZipcodeSearchEngine

# [END imports]

# [START create_app]
app = Flask(__name__)

# [END create_app]

def _validate_population_json():
    fields = ['longitude', 'latitude', 'radius']
    if not request.json or any(x not in request.json for x in fields):
        abort(400)


@app.route('/')
def index():
    return "Go to the REST endpoint to check the app."


# remember to set 'Content-Type': 'application/json' on your POST request
@app.route('/api/v1.0/population', methods=['POST'])
def get_population():
    _validate_population_json()
    res = ZipcodeSearchEngine().by_coordinate(request.json['longitude'], request.json['latitude'], radius=request.json['radius'])
    population = 0
    for zip_code in res:
        population += zip_code["Population"]

    return jsonify({'population': population}), 201


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]

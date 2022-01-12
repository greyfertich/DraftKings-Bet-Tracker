#!/usr/bin/python3
from flask import Flask
from flask_restful import Resource, Api, reqparse
from espn_api import Espn_api

app = Flask(__name__)
api = Api(app)
api.add_resource(Espn_api, '/espn')  # '/users' is our entry point for Users

if __name__ == '__main__':
    app.run(debug=False)  # run our Flask app

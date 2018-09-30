# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:04:28 2018

@author: Camille
"""

from flask import Flask
from flask_moment import Moment
from flask_cors import CORS

moment = Moment()
app = None


def create_app():
    global app
    app = Flask(__name__)
    CORS(app)
    moment.init_app(app)

    from .api import init_api
    init_api(app)

    return app
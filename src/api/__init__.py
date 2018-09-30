# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:05:08 2018

@author: Camille
"""

from flask_restplus import Api

api = None


def init_api(app):
    global api
    api = Api(app, validate=True)

    from src.api import GET_spiral_matrix
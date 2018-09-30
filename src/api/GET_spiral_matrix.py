# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:06:51 2018

@author: Camille
"""

from src.api import api

from flask import request
from flask_restplus import Resource
from flask_restplus import fields
from src.model.main_spiral import spiral_matrix


@api.route('/model/main_spiral')
class MainSpiral(Resource):
    @api.doc('Returns a nxn spiral matrix with a 1 in [n,n] position')
    @api.expect(api.model('MainSpiral', {
        'eleve_id': fields.String,
        'lecon_id': fields.String
    }))
    @api.response(200, 'Success')
    def get(self,k):
        return {spiral_matrix(k)}
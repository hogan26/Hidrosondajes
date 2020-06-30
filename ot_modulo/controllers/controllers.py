# -*- coding: utf-8 -*-
from odoo import http
    

class OtModulo(http.Controller):
    @http.route('/ot_modulo/ot_modulo/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/ot_modulo/ot_modulo/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('ot_modulo.listing', {
            'root': '/ot_modulo/ot_modulo',
            'objects': http.request.env['ot_modulo.ot_modulo'].search([]),
        })

    @http.route('/ot_modulo/ot_modulo/objects/<model("ot_modulo.ot_modulo"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('ot_modulo.object', {
            'object': obj
        })

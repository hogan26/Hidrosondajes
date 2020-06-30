# -*- coding: utf-8 -*-

from odoo import models, fields, api
from unidecode import unidecode
    

class ot_modulo(models.Model):
    _name = 'ot_modulo.ot_modulo'
    _description = 'ot_modulo.ot_modulo'

    id_ot = fields.Integer()
    name = fields.Char()
    cliente = fields.Char()
    estado = fields.Char()
    equipo = fields.Char()
    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    descripcion = fields.Text()
    #agregando un nuevo campo... campo de fecha y hora
    fecha = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    
    @api.model
    def create(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(ot_modulo, self).create(values)

    def write(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(ot_modulo, self).write(values)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

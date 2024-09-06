from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model.dept'
    _description = 'My Basic Model'


    name = fields.Char(string='Name', required=True)
    age = fields.Float(string='Age')
    roll_number = fields.Integer(string='Roll Number')

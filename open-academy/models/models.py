# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = "course.course"
    _description = "open-academy.open-academy"

    title = fields.Char(required=True)
    description = fields.Char()


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

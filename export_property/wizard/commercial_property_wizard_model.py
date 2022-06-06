from odoo import models, fields, api
import os
import base64
from os.path import abspath, dirname
import paramiko
from datetime import datetime


class CommercialPropertyWizard(models.TransientModel):
    _name = 'commercial.wizard'

    file = fields.Many2many("ir.attachment", 'res_name')

    def save_commercial_file(self):
        print(self.env.context)
        print('Commercial Saved')

    def action_get_file(self):
        print('Helooo')

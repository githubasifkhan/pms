from odoo import models, fields, api


class ResidentialPropertyWizard(models.TransientModel):
    _name = 'residential.wizard'

    file = fields.Binary(string='File')

    def save_residential_file(self):
        print('Residential Saved')

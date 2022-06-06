from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CRMLeadFields(models.Model):
    _inherit = 'crm.lead'

    country_id = fields.Many2one('res.country' , string="Country")
    nationality_id = fields.Many2one('res.country' , string="Nationality")
    area = fields.Many2one('area.details',string="Area")

    property_type_id = fields.Many2one('property.type' , string="Property Type" , required=True)
    transaction_type = fields.Selection([
        ('lease', 'Lease'),
        ('rent', 'Rent'),
        # ('sold', 'Sold'),
        # ('rent', 'Rented'),
        # ('transaction_pending', 'Transaction Pending'),
        # ('valuation', 'Valuation'),
    ])

    no_of_bedrooms = fields.Selection(selection=[(f'a{i}', i) for i in range(1,21)], string='No of Bedrooms')
    no_of_bathrooms = fields.Selection(selection=[(f'a{i}', i) for i in range(1,21)], string='No of Bathrooms')
    # no_of_bedrooms = fields.Integer(string='No.of Bedrooms')
    # no_of_bathrooms = fields.Integer(string='No.of Bathrooms')
    size_in_sqft = fields.Float(string='Size In Sqft')
    size_in_sqm = fields.Float(string='Size In Sqm' , force_save="1")
    no_of_parkings = fields.Integer(string='No. of Parkings')
    budget_from = fields.Integer(string='Budget From')
    budget_to = fields.Integer(string='Budget To')

    crm_media_id = fields.Many2many(comodel_name="ir.attachment",
                                    relation="m2m_ir_crm_media_rel",
                                    column1="m2m_id",
                                    column2="attachment_id",
                                    )

    @api.onchange('size_in_sqft')
    def set_value_sqft(self):
        self.size_in_sqm = self.size_in_sqft * 0.092903
        # a = 0.092903
        # self.size_in_sqft = a
        # print("heloooooooooooooooooooooooo")

    @api.onchange('size_in_sqm')
    def set_value_sq(self):
        self.size_in_sqft = self.size_in_sqm / 0.092903























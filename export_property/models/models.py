# -*- coding: utf-8 -*-
from os.path import dirname, abspath

from odoo import models, fields, api
import xml.etree.cElementTree as e
from datetime import datetime
from odoo.tools.image import image_data_uri
import base64


class CommercialPropertyInh(models.Model):
    _inherit = 'commercial.property'

    def get_data(self):
        records = self.env['commercial.property'].search([])
        r = e.Element("list")
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        r.set('last_update', date_time)
        for rec in records:
            property = e.SubElement(r, "property")
            w = rec.write_date
            write_date = w.strftime("%Y-%m-%d %H:%M:%S")
            property.set('last_update', write_date)
            e.SubElement(property, "reference_number").text = rec.reference_number
            e.SubElement(property, "permit_number").text = rec.permit_number
            e.SubElement(property, "offering_type").text = rec.offering_type
            e.SubElement(property, "property_type").text = str(rec.property_type_id.property_type)
            e.SubElement(property, "price_on_application").text = "Yes" if rec.price_on_application else "No"
            e.SubElement(property, "city").text = rec.city
            e.SubElement(property, "community").text = rec.community
            e.SubElement(property, "property_name").text = rec.property_name
            e.SubElement(property, "title_en").text = rec.title_en
            e.SubElement(property, "description_en").text = rec.description_en
            e.SubElement(property, "size").text = str(rec.size)
            e.SubElement(property, "bedroom").text = str(rec.bedroom)
            e.SubElement(property, "bathroom").text = str(rec.bathroom)

            agent = e.SubElement(property, "agent")
            e.SubElement(agent, "id").text = str(rec.agent.id) if str(rec.agent.id) else ''
            e.SubElement(agent, "name").text = str(rec.agent.name) if str(rec.agent.name) else ''
            e.SubElement(agent, "email").text = str(rec.agent.email) if str(rec.agent.email) else ''
            e.SubElement(agent, "phone").text = str(rec.agent.phone) if str(rec.agent.phone) else ''
            # e.SubElement(agent, "photo").text = image_data_uri(rec.agent.photo) if rec.agent.photo else ''
            e.SubElement(agent, "licence_no").text = 'None'
            e.SubElement(agent, "info").text = 'None'

            e.SubElement(property, "completion_status").text = str(rec.build_completion_status)
            e.SubElement(property, "parking").text = str(rec.parking)
            e.SubElement(property, "furnished").text = str(rec.furnished)
            e.SubElement(property, "sub_community").text = rec.sub_community
            e.SubElement(property, "private_amenities").text = rec.private_amenities
            e.SubElement(property, "price").text = str(rec.for_sale_price)

            photo1 = e.SubElement(property, "photo")
            e.SubElement(photo1, "url").text = image_data_uri(rec.image1) if rec.image1 else ''
            photo2 = e.SubElement(property, "photo")
            e.SubElement(photo2, "url").text = image_data_uri(rec.image2) if rec.image2 else ''
            photo3 = e.SubElement(property, "photo")
            e.SubElement(photo3, "url").text = image_data_uri(rec.image3) if rec.image3 else ''
            photo4 = e.SubElement(property, "photo")
            e.SubElement(photo4, "url").text = image_data_uri(rec.image4) if rec.image4 else ''
            photo5 = e.SubElement(property, "photo")
            e.SubElement(photo5, "url").text = image_data_uri(rec.image5) if rec.image5 else ''
            photo6 = e.SubElement(property, "photo")
            e.SubElement(photo6, "url").text = image_data_uri(rec.image6) if rec.image6 else ''
            photo7 = e.SubElement(property, "photo")
            e.SubElement(photo7, "url").text = image_data_uri(rec.image7) if rec.image7 else ''
            photo8 = e.SubElement(property, "photo")
            e.SubElement(photo8, "url").text = image_data_uri(rec.image8) if rec.image8 else ''
            photo9 = e.SubElement(property, "photo")
            e.SubElement(photo9, "url").text = image_data_uri(rec.image9) if rec.image9 else ''
            photo10 = e.SubElement(property, "photo")
            e.SubElement(photo10, "url").text = image_data_uri(rec.image10) if rec.image10 else ''
        a = e.ElementTree(r)
        loc = abspath(dirname(dirname(dirname(__file__)))) + '/export_property/demo/json_to_xml_commercial_property.xml'
        a.write(loc)
        return a

    def action_commercial_wizard(self):
        b = self.get_data()
        loc = abspath(
            dirname(dirname(dirname(__file__)))) + '/export_property/demo/json_to_xml_commercial_property.xml'
        file = open(loc, "rb")
        out = file.read()
        c = self.env['ir.attachment'].create({
            'name': 'File',
            'type': 'binary',
            'datas': base64.b64encode(out),
            # 'res_model': ._name,
            # 'res_id': self.id
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Export Commercial Properties',
            'view_id': self.env.ref('export_property.view_commercial_wizard', False).id,
            'target': 'new',
            'context': {'default_file': [c.id]},
            'res_model': 'commercial.wizard',
            'view_mode': 'form',
        }


class ResidentialPropertyInh(models.Model):
    _inherit = 'residential.property'

    def get_data(self):
        records = self.env['residential.property'].search([])
        r = e.Element("list")
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        r.set('last_update', date_time)
        for rec in records:
            property = e.SubElement(r, "property")
            w = rec.write_date
            write_date = w.strftime("%Y-%m-%d %H:%M:%S")
            property.set('last_update', write_date)
            e.SubElement(property, "reference_number").text = rec.reference_number
            e.SubElement(property, "permit_number").text = rec.permit_number
            e.SubElement(property, "offering_type").text = rec.offering_type
            e.SubElement(property, "property_type").text = str(rec.property_type_id.property_type)
            e.SubElement(property, "price_on_application").text = "Yes" if rec.for_sale_price_on_app else "No"
            e.SubElement(property, "city").text = rec.city
            e.SubElement(property, "community").text = rec.community
            e.SubElement(property, "property_name").text = rec.property_name
            e.SubElement(property, "title_en").text = rec.title_en
            e.SubElement(property, "description_en").text = rec.description_en
            e.SubElement(property, "size").text = str(rec.size)
            e.SubElement(property, "bedroom").text = str(rec.bedroom)
            e.SubElement(property, "bathroom").text = str(rec.bathroom)

            agent = e.SubElement(property, "agent")
            e.SubElement(agent, "id").text = str(rec.agent.id) if str(rec.agent.id) else ''
            e.SubElement(agent, "name").text = str(rec.agent.name) if str(rec.agent.name) else ''
            e.SubElement(agent, "email").text = str(rec.agent.email) if str(rec.agent.email) else ''
            e.SubElement(agent, "phone").text = str(rec.agent.phone) if str(rec.agent.phone) else ''
            # e.SubElement(agent, "photo").text = image_data_uri(rec.agent.photo) if rec.agent.photo else ''
            e.SubElement(agent, "licence_no").text = 'None'
            e.SubElement(agent, "info").text = 'None'

            e.SubElement(property, "completion_status").text = str(rec.build_completion_status)
            e.SubElement(property, "parking").text = str(rec.parking)
            e.SubElement(property, "furnished").text = "Yes" if rec.furnished else "No"
            e.SubElement(property, "sub_community").text = rec.sub_community
            e.SubElement(property, "private_amenities").text = rec.private_amenities
            e.SubElement(property, "price").text = str(rec.for_rent_price)

            photo1 = e.SubElement(property, "photo")
            e.SubElement(photo1, "url").text = image_data_uri(rec.image1) if rec.image1 else ''
            photo2 = e.SubElement(property, "photo")
            e.SubElement(photo2, "url").text = image_data_uri(rec.image2) if rec.image2 else ''
            photo3 = e.SubElement(property, "photo")
            e.SubElement(photo3, "url").text = image_data_uri(rec.image3) if rec.image3 else ''
            photo4 = e.SubElement(property, "photo")
            e.SubElement(photo4, "url").text = image_data_uri(rec.image4) if rec.image4 else ''
            photo5 = e.SubElement(property, "photo")
            e.SubElement(photo5, "url").text = image_data_uri(rec.image5) if rec.image5 else ''
            photo6 = e.SubElement(property, "photo")
            e.SubElement(photo6, "url").text = image_data_uri(rec.image6) if rec.image6 else ''
            photo7 = e.SubElement(property, "photo")
            e.SubElement(photo7, "url").text = image_data_uri(rec.image7) if rec.image7 else ''
            photo8 = e.SubElement(property, "photo")
            e.SubElement(photo8, "url").text = image_data_uri(rec.image8) if rec.image8 else ''
            photo9 = e.SubElement(property, "photo")
            e.SubElement(photo9, "url").text = image_data_uri(rec.image9) if rec.image9 else ''
            photo10 = e.SubElement(property, "photo")
            e.SubElement(photo10, "url").text = image_data_uri(rec.image10) if rec.image10 else ''
        a = e.ElementTree(r)
        loc = abspath(
            dirname(dirname(dirname(__file__)))) + '/export_property/demo/json_to_xml_residential_property.xml'
        a.write(loc)
        return a

    def action_residential_wizard(self):
        b = self.get_data()
        loc = abspath(
            dirname(dirname(dirname(__file__)))) + '/export_property/demo/json_to_xml_residential_property.xml'
        file = open(loc, "rb")
        out = file.read()
        r = self.env['ir.attachment'].create({
            'name': 'File',
            'type': 'binary',
            'datas': base64.b64encode(out),
            # 'res_model': ._name,
            # 'res_id': self.id
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Export Residential Properties',
            'view_id': self.env.ref('export_property.view_residential_wizard', False).id,
            'target': 'new',
            'context': {'default_file': [r.id]},
            'res_model': 'residential.wizard',
            'view_mode': 'form',
        }

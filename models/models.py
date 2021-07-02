# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MultiStepForm(models.Model):
    _name = 'multi.step.form'
    _rec_name = 'fname'
    _description = 'Multi step form'

    # Step 1 form
    fname = fields.Char(string="First Name", required=False, )
    lname = fields.Char(string="Last Name", required=False, )
    phone = fields.Char(string="Phone", required=False, )

    # Step 2 form
    twitter = fields.Char(string="Twitter", required=False, )
    facebook = fields.Char(string="Facebook", required=False, )
    gplus = fields.Char(string="Google Plus", required=False, )

    # Step 3 form
    email = fields.Char(string="Email", required=False, )
    password = fields.Char(string="Password", required=False, )

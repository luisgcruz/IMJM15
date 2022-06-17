# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductSatCode(models.Model):
    _inherit = 'l10n_mx_edi.product.sat.code'

    aceptable = fields.Boolean(help='Si no es aceptable, rechazará el intento de crear la factura desde el portal.', default=False)
# -*- coding: utf-8 -*-
from odoo.tests import common
from odoo.tools import mute_logger


class TestProductMaterial(common.TransactionCase):

    def test_min_price(self):
        """ Test minimal buy price for product, error expected to raise if price by is under 100"""

        type_id = self.env.ref("product_material.material_type_fabric").id
        with self.assertRaises(Exception, msg="Error expected, but none raises"), mute_logger('odoo.sql_db'):
            self.env['product.material'].create({
                'code': 'test_code',
                'name': 'test_code',
                'type_id': type_id,
                'price_buy': 99,
                'supplier_id': 1,
            })

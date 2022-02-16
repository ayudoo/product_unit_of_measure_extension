from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    sales_count = fields.Float(
        compute="_compute_sales_count",
        string="Sold",
        digits="Product Unit of Measure",
    )

    purchased_product_qty = fields.Float(
        compute="_compute_purchased_product_qty",
        string="Purchased",
        digits="Product Unit of Measure",
    )

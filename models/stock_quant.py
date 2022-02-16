from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    inventory_quantity = fields.Float(
        "Inventoried Quantity",
        compute="_compute_inventory_quantity",
        inverse="_set_inventory_quantity",
        groups="stock.group_stock_manager",
        digits="Product Unit of Measure",
    )

    available_quantity = fields.Float(
        "Available Quantity",
        help=(
            "On hand quantity which hasn't been reserved on a transfer, in the default"
            + " unit of measure of the product"
        ),
        compute="_compute_available_quantity",
        digits="Product Unit of Measure",
    )

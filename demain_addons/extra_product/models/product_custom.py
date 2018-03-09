import logging
import base64
from openerp import api, models, fields
from openerp.tools.translate import _
from openerp.exceptions import Warning
_logger = logging.getLogger(__name__)

class myProduct(models.Model):

    _inherit = 'product.template'

    column_one = fields.Char('Name one')

    column_two = fields.Integer('Name two')

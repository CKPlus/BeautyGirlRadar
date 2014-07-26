from flask import Blueprint

blueprint_bgradar = Blueprint(
    'bgradar',
    __name__,
    template_folder='templates')

import views
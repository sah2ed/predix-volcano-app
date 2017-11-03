
from flask import Blueprint

# Templates are rendered with Jinja2 and static files are delivered as is,
# though would be better from a web server like nginx.
dashboard = Blueprint('dashboard', __name__, template_folder='templates',
        static_folder='dist')

# views.py defines routes defined by this Flask Blueprint
from . import views


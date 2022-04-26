#handlers.py  setting up own error handlers
from flask import Blueprint, render_template

# create a blueprint
error_pages = Blueprint('error_pages',__name__)

#not found error - 404
@error_pages.app_errorhandler(404)
def  error_404(error):
    return render_template('error_pages/404.html'), 404

#access forbidden error - 403
@error_pages.app_errorhandler(404)
def  error_404(error):
    return render_template('error_pages/403.html'), 403
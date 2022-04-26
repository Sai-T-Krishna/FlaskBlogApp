# blogProject init file

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'saikrishna'

#########################################
############     DATABASE      ##########
#########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## create database object and pass in the app
db = SQLAlchemy(app)
Migrate(app, db)

########################################
###########   Login configuratons  ###########

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


#import core blueprint from /core/views.py

from BlogProject.core.views import core
from BlogProject.error_pages.handlers import error_pages
from BlogProject.users.views import users
from BlogProject.Blogposts.views import blog_posts
#registering the blueprint

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)

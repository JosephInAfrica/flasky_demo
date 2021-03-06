from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config

bootstrap=Bootstrap()
mail=Mail()
moment=Moment()
db=SQLAlchemy()
pagedown=PageDown()

login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'



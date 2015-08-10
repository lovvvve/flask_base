from flask import Flask

from __init__ import make_app
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from views.admin import MyView, MyDBView
from models import User
from extensions import db
import os.path as op
from flask.ext.admin.contrib.fileadmin import FileAdmin
from flask.ext.admin.model import BaseModelView



from flask.ext.sqlalchemy import SQLAlchemy



if __name__ == '__main__':
    app = make_app(debug=True, port=8080)
    admin = Admin(app)
    admin.add_view(MyView(name="Hello"))
    admin.add_view(ModelView(User, db.session))


    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path, '/static/', name='static'))
    app.debug = True
    app.run()

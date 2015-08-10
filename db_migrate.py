#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Lovvvve'
__email__ = 'lovvvve+github@gmail.com'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from __init__ import make_app
from extensions import db

app = make_app(debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:flask@localhost/test'

# db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import User

# class User1(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

if __name__ == '__main__':
    # db.create_all()
    manager.run()


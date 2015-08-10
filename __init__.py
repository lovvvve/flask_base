#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Lovvvve'
__email__ = 'lovvvve+github@gmail.com'

from os.path import basename, dirname
from sys import argv

from flask import Flask, request, g, session
from flask import Blueprint, render_template

from views import dashboard
from models import *
from extensions import db


APP_NAME = basename(dirname(argv[0]))

MODULES = (
    (dashboard, "/"),
    (dashboard, '/a'),
)


def make_app(debug=True, port=80):
    modules = MODULES
    app = Flask(APP_NAME)
    # app.config.from_pyfile(config)
    app.debug = debug
    app.secret_key= "gqZcgcxAJxe2H9xxxLzAQK"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:flask@localhost/test'
    configure_blueprints(app, modules)
    configure_extensions(app)

    return app


def configure_blueprints(app, modules):
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)


def configure_extensions(app):
    db.app = app
    db.init_app(app)
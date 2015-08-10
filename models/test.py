#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Lovvvve'
__email__ = 'lovvvve+github@gmail.com'

from extensions import db
from sqlalchemy.sql import func



class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    uptime = db.Column(db.DateTime(timezone=True), default=func.now())



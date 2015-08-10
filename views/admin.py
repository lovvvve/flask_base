#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Lovvvve'
__email__ = 'lovvvve+github@gmail.com'

from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from models import User



class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('dashboard/dashboard.html')


class MyDBView(ModelView):

    can_create = False
    column_list = ('id', 'name')

    def __init__(self, session, **kwargs):
        super(MyDBView, self).__init__(User, session, **kwargs)

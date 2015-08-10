#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Lovvvve'
__email__ = 'lovvvve+github@gmail.com'

from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def dashboard_page():
    return render_template('dashboard/dashboard.html')

    # return "Hello world!"
@dashboard.route('/a')
def a_page():
    return render_template('dashboard/dashboard.html')


@dashboard.route('/a/a')
def aa_page():
    return render_template('dashboard/dashboard.html')
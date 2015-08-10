#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Lovvvve'
__email__ = 'lovvvve+github@gmail.com'

from flask import render_template, request, jsonify
from __init__ import make_app
import sys
from gevent.pywsgi import WSGIServer
from flask.ext.script import Manager

app = make_app(debug=True)

manager = Manager(app)


# if __name__ == '__main__':
#     if len(sys.argv) == 2 and sys.argv[1] == 'run':
#         # debug == True
#         port = 8080
#         host = '0.0.0.0'
#
#     app = make_app(debug=True)
#     app.config['PORT'] = port
#
#     http_server = WSGIServer((host, port),
#                              app,
#     )
#     http_server.serve_forever()

@manager.command
def hello():
    print "hello"


if __name__ == '__main__':
    manager.run()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pivotal.py
# @Author: lucas
# @Date  : 10/1/18
# @Desc  :

from flask import Flask
from flask_restful import Resource, Api
from app.handler.base import generate_short_url, get_original_url

app = Flask(__name__)

api = Api(app)


class ShortUrlResource(Resource):
    def get(self, todo_id):
        import random
        import sys
        import pprint
        pprint.pprint(todo_id)
        return {'random_id': random.randint(0, sys.maxint)}


api.add_resource(ShortUrlResource, '/<string:todo_id>')


@app.route('/')
def ping():
    return 'pong'


@app.route('/generate')
def short(original_url):
    t_short_url = generate_short_url(original_url)
    return t_short_url


@app.route('/original/<short_url>')
def original(short_url):
    original_url = get_original_url(short_url)
    return str(original_url)


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pivotal.py
# @Author: lucas
# @Date  : 10/1/18
# @Desc  :

from flask import Flask
from flask import request, redirect
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


@app.route('/api/test', methods=['POST', 'GET'])
def generate():
    import random
    import string
    short_urls = []
    for x in range(100):
        chars = [random.choice(string.lowercase) for x in range(10)]
        random_str = ''.join(chars)
        url = 'http://%s.com' % random_str
        result = generate_short_url(url)

        result_url = 'http://short.localhost.com:8000/short/%s' % result
        short_urls.append(result_url)

    return str(short_urls)


@app.route('/api/generate', methods=['POST'])
def short():
    original_url = request.args.get('url')
    if not original_url:
        return
    t_short_url = generate_short_url(original_url)
    return str(t_short_url)


@app.route('/short/<short_url>', methods=['GET'])
def original(short_url):
    original_url = get_original_url(short_url)
    return redirect(original_url)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

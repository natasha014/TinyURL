from flask import Flask, request, jsonify, render_template
from flask.helpers import send_from_directory
from flask.wrappers import Request, Response
from flask import request
import helper
import json

app = Flask(__name__)

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '/static/swagger.json') 


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')


@app.route('/ping')
def ping():
    return Response(status=200)

@app.route('/generateShortURL')
def generate_url():
    try:
        long_url = request.args.get('inputURL')
        username = request.args.get('username')
        if(long_url is None or username is None):
            return Response(status=400, response='Bad request', mimetype='text/plain')
        shorten = helper.create_hash(long_url,username)
        return Response(status=200, response=shorten, mimetype='text/plain')
    except ValueError as error:
        print(error,flush=True)
        return Response(status=400,mimetype='text/plain',response='Long url already exists' )
    except Exception as error:
        print(error,flush=True)
        return Response(status=500)

@app.route('/getLongURL')
def get_long_url():
    try:
        short_url = request.args.get('shortURL')
        if(short_url is None):
            return Response(status=400, response='Bad request', mimetype='text/plain')
        long_url = helper.get_long_url(short_url)
        return Response(status=200, mimetype='text/plain',response=long_url)
    except KeyError as error:
        print(error,flush=True)
        return Response(status=404)
    except Exception as error:
        print(error,flush=True)
        return Response(status=500)


@app.route('/getUsage')
def get_url_usage():
    try:
        short_url = request.args.get('shortURL')
        if(short_url is None):
            return Response(status=400, response='Bad request', mimetype='text/plain')
        url_usage = helper.get_url_usage(short_url)
        return Response(status=200, mimetype='application/json', response=json.dumps(url_usage))
    except KeyError as error:
        print(error,flush=True)
        return Response(status=404)
    except Exception as error:
        print(error,flush=True)
        return Response(status=500)

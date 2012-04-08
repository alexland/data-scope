#!/usr/local/bin/python2.7
# encoding: utf-8

from __future__ import absolute_import
import time
import flask as FK
from redis import Redis as redis
from contextlib import closing
import numpy as NP

DEBUG=True
REDIS_DB = 2
DEBUG = True
SECRET_KEY = "!Erew9reQir549&3d394W*"
USERNAME = None
PASSWORD = None
REDIS_HOST = 'localhost'
PORT = 6379
# RESOURCE_PATH="/Users/doug/Dropbox/WebDev"

app = FK.Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('DATASCOPE_SETTINGS')


def connect_db():
	return redis(db=REDIS_DB, host=REDIS_HOST, port=PORT)


@app.before_request
def before_request():
	FK.g.db = connect_db()


@app.route('/_playPro')
def playPro():
	return FK.render_template('playPro.html')


@app.route('/_fromDB')
def fromDB():
	v = range(int(time.time()), int(time.time()) + int(5e5), 1000)
	x = NP.linspace(0, 5, 500)
	y = 1 + NP.sin(x)
	nx = NP.random.normal(0, .05, 500)
	y += nx
	d = [ { 'x':t[0], 'y':t[1] } for t in zip(v, y) ]
	return FK.jsonify(result = d)


@app.route('/_fromDB1')
def fromDB1():
	v = range(int(time.time()), int(time.time()) + int(5e5), 1000)
	x = NP.linspace(0, 5, 500)
	y = 1 + NP.sin(x/2)
	nx = NP.random.normal(0, .05, 500)
	y += nx
	d = [ { 'x':t[0], 'y':t[1] } for t in zip(v, y) ]
	return FK.jsonify(result = d)


@app.route('/_fromDB2')
def fromDB2():
	v = range(int(time.time()), int(time.time()) + int(5e5), 1000)
	x = NP.linspace(0, 5, 500)
	y = 1 + NP.cos(x)
	nx = NP.random.normal(0, .05, 500)
	y += nx
	d = [ { 'x':t[0], 'y':t[1] } for t in zip(v, y) ]
	return FK.jsonify(result = d)


@app.route('/_fromDB3')
def fromDB3():
	v = range(int(time.time()), int(time.time()) + int(5e5), 1000)
	x = NP.linspace(0, 5, 500)
	y = 1 + NP.cos(x/2.)
	nx = NP.random.normal(0, .05, 500)
	y += nx
	d = [ { 'x':t[0], 'y':t[1] } for t in zip(v, y) ]
	return FK.jsonify(result = d)


@app.route('/_fromDB0')
def fromDB0():
	x = NP.linspace(0, 5, 500)
	y = 3*NP.sin(x/2.2) + 1
	nx = .03 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB01')
def fromDB01():
	x = NP.linspace(0, 5, 500)
	y = 5*NP.sin(x/4.6) + 1
	nx = .1 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB02')
def fromDB02():
	x = NP.linspace(0, 5, 500)
	y = NP.sin(1.8*x) + 1
	nx = .1 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB03')
def fromDB03():
	x = NP.linspace(0, 5, 500)
	y = 2.2 * NP.sin(x/.5) + 1
	nx = .05 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB04a')
def fromDB04a():
	x = NP.linspace(0, 5, 500)
	y = 1.5 * NP.sin(x/2.8) + 2.
	nx = .1 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB04b')
def fromDB04b():
	x = NP.linspace(0, 5, 500)
	y = NP.cos(x/2.4) + 2
	nx = .02 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB04c')
def fromDB04c():
	x = NP.linspace(0, 5, 500)
	y = 4.4 * NP.sin(x/3.7) + 4
	nx = .075 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB04d')
def fromDB04d():
	x = NP.linspace(0, 5, 500) + 1
	y = 3.8 * NP.cos(x/4.8)
	nx = .05 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB05a')
def fromDB05a():
	x = NP.linspace(0, 5, 500)
	y = NP.sin(x) + 1.75
	nx = .03 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB05b')
def fromDB05b():
	x = NP.linspace(0, 5, 500)
	y = 2.5 * NP.sin(x) + 1.75
	nx = .05 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/_fromDB05c')
def fromDB05c():
	x = NP.linspace(0, 5, 500)
	y = 2.5 * NP.sin(3*x) + 1.75
	nx = .05 * NP.random.randn(500)
	y += nx
	d = y.tolist()
	return FK.jsonify(result = d)


@app.route('/')
def index():
	return FK.render_template('index-1.html')



if __name__ == '__main__':
	app.debug = True
	app.run()

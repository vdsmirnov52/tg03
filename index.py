#!/usr/bin/python -u
# -*- coding: utf-8 -*-

# все импорты
import os, time
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from pylib import dbtools

app = Flask(__name__)
app.config.from_object(__name__)

# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть
# значений через переменную окружения
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'users.db'),
	DEBUG=True,
	SECRET_KEY='development key',
#	PERMANENT_SESSION_LIFETIME=120, 
	ULOGIN='admin',
	PASSWORD='123Admin',
	TITLE=u'Городец',
#	DB_GSMP='host=10.40.25.176 dbname=vms_ws port=5432 user=vms'
	DB_GSMP='host=212.193.103.20 dbname=b03 port=5432 user=smirnov'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_pg (ddd = 'host=localhost dbname=b03 port=5432'):
	g.dbrec = dbtools.dbtools(ddd)
	return g.dbrec
	if db and db.last_error:
		print "Ok"
		return db

def	is_person (ulogin, password):
	flash (u'Отсутствуют login: %s  password: %s' % (ulogin, password))
	if not (ulogin and password):
		return	False	#render_template('login.html', error=u'Отсутствую login или password')
	return	True	#"is_person (%s %s)" % (ulogin, password)

@app.route('/set', methods=['POST'])
def	set_entry():
	error = None
	if request.form.get('nsi_opts') in ['person', 'autos', 'norms']:
		opts_name = request.form.get('nsi_opts')
		session['nsi_opts'] = opts_name
		if opts_name == 'person':
			opts = [{'name': 'NNN', 'test': 'TTT'}, {'name': 'nnn 2', 'test': 'ttt 2'}]
		else:	opts = render_template('list_autos.html')
		return render_template('nsi.html', error=error, opts=opts)
	else:
		session['nsi_opts'] = None
		flash(str(request))
		return render_template('nsi.html', error=error)
#	return	"set_entry %s" % str(request)

@app.route('/')
def	index ():
#	return	"<h1>Index t03</h1> %s: %s" % (app.config['DB_GSMP'], connect_pg (app.config['DB_GSMP']))
	sdate = time.strftime("%d-%m-%Y %T", time.localtime(time.time()))
	g.sdate = sdate
	if session.get('logged_in'):
		return render_template('index.html')
	else:	return render_template('login.html', sdate=g.sdate)

@app.route('/login', methods = ['GET', 'POST'])
def login ():
	error = None
	if request.method == 'POST':
		if (request.form['ulogin'] == app.config['ULOGIN']) and (request.form['password'] == app.config['PASSWORD']):
			session['logged_in'] = True
			flash(u'Вы вошли в систему администрирования НСИ')
			return redirect(url_for('nsi'))
		elif is_person (request.form['ulogin'], request.form['password']):
			session['logged_in'] = True
			return redirect(url_for('index'))
		else:
			error = u'Ошибка входа в систему!'
	return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
#	flash(u'Вы вышли из системы')	#'You were logged out')
	return redirect(url_for('index'))

import	json
@app.route('/nsi', methods=['GET', 'POST'])
def	nsi ():
#	return	"Вы вошли в систему администрирования НСИ"
	error = None
	return render_template('nsi.html', error=error)

@app.route('/ajax', methods=['GET', 'POST'])
def	ajax_html():
	if request.method == 'POST':
		name = request.form['name'];
		return json.dumps({'len': session.get('logged_in')})	#len(name)})
	return render_template('ajax.html')

def test ():
	with app.test_request_context():
		print url_for('index')
		print url_for('login')
		print url_for('login', next = 'hello', usr_id = '123')


if __name__ == '__main__':
	#test ()
	app.run(host='0.0.0.0')

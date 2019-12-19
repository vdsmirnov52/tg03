# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, url_for, current_app, session, redirect, request, flash
from jinja2 import TemplateNotFound
from werkzeug.local import LocalProxy

import time, os
import forms

main_page = Blueprint('main_page', __name__, template_folder= '../../templates')	#'/templates')

'''
'''


def sout_row (row, **keywords):
	ss = []
	if not keywords:
		for s in row: ss.append(str(s))
	else:
		for k in keywords.keys():
			ss.append("%s: '%s'" % (k, keywords[k]))
	return '\t'.join(ss)
	
def get_data():
	from run import get_db
	idb = LocalProxy(get_db)
	query = "SELECT * FROM vperson_sp WHERE n_pst IN (1,2)"
	rows = idb.get_rows(query)
	if not rows:    return "Not data"
	ress = ["<pre>"]
	for r in rows:
		ress.append(sout_row(r)) #, format='default'))
	ress.append("</pre>")
	return "\n".join(ress)


@main_page.route('/', defaults = {'page': 'index'})
@main_page.route('/<page>', methods = ['POST'])
def show(page):
	sdate = time.strftime("%T %d-%m-%Y", time.localtime(time.time()))
	pname = '%s.html' % page
	# print "main_page", page, os.system("ls -l %s/*" % main_page.static_folder)
	flash('%s %s %s' % (sdate, page, request.method))
	flash("%s" % request.form)
	# for k in current_app.config.keys(): print '%32s =' % k, current_app.config[k]
	# for k in os.environ.keys():     print "%32s =" % k, os.environ[k]
	# for k in env.keys():     print "%32s =" % k, env[k]
	if session.get('logged_in'):
		# return "@main_page.route %s" % pname
		if page == 'ajax':
			sajax = ["curr_dtime|%s" % sdate, "events| %s" % dict(request.form)]
			ss = dict(request.form).get('shstat')
			print "\tSS", ss
			if ss and ss[0] == 'KuKu':  sajax.append("my_body| %s" % render_template('test.html'))
			if ss and ss[0] == 'CLL_OPER':  sajax.append("my_body| %s" % get_data())
			return '~'.join(sajax)
			# return "~curr_dtime| %s ~events| %s" % (sdate, dict(request.form))
		return render_template('test.html')
	else:
		val = ('123', 'ZZZ')
		form = forms.PersonForm('values', disp=321, name=u'Иванов')
		return render_template('rem.html', form=form)

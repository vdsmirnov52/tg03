# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, url_for, current_app, session, redirect, request, flash
from jinja2 import TemplateNotFound

import time, os
import forms

main_page = Blueprint('main_page', __name__,
			template_folder= '../../templates')	#'/templates')
'''

'''

@main_page.route('/', defaults = {'page': 'index'})
@main_page.route('/<page>', methods = ['POST'])
def show(page):
#	from run import app
	sdate = time.strftime("%d-%m-%Y %T", time.localtime(time.time()))
	pname = '%s.html' % page
	# print "main_page", page, os.system("ls -l %s/*" % main_page.static_folder)
	flash('%s %s %s' % (sdate, page, request.method))
	flash("%s" % request.form)
	# for k in current_app.config.keys(): print '%32s =' % k, current_app.config[k]
	# for k in os.environ.keys():     print "%32s =" % k, os.environ[k]
	# for k in env.keys():     print "%32s =" % k, env[k]
	if session.get('logged_in'):
		# return "@main_page.route %s" % pname
		return render_template('test.html')
	else:
		val = ('123', 'ZZZ')
		form = forms.PersonForm('values', disp=321, name=u'Иванов')
		return render_template('rem.html', form=form)

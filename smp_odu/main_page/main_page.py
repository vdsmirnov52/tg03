# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, url_for, current_app, session, redirect, request, flash
from jinja2 import TemplateNotFound

import time, os

main_page = Blueprint('main_page', __name__,
			template_folder= '../../templates')	#'/templates')
'''

'''

@main_page.route('/', defaults={'page': 'index'})
@main_page.route('/<page>')
def show(page):
#	from run import app
	pname = '%s.html' % page
	print "main_page", page, os.system("ls -l %s/*" % main_page.static_folder)
	if session.get('logged_in'):
		# return "@main_page.route %s" % pname
		return render_template('test.html')
	else:
		return render_template('rem.html')

# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__, root_path='/home/smirnov/PycharmProjects/g03', static_folder='static',
                        template_folder='/home/smirnov/PycharmProjects/g03/templates')
'''
@simple_page.route('/')
def rrr():
    return render_template('rem.html')
    return "Z"*33
'''

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    pname = '%s.html' % page
    # return "Hello %s !" % pname
    try:
        print "ZZZ", pname
        return render_template('rem.html', data=pname)
    except TemplateNotFound:
        abort(404)

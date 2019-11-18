# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__, static_folder='/static',
                        template_folder='/templates')

@simple_page.route('/')
def rrr():
    return "Z"*33

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    pname = '%s.html' % page
    # return "Hello %s !" % pname
    try:
        print "ZZZ", pname
        return render_template(pname)
    except TemplateNotFound:
        abort(404)

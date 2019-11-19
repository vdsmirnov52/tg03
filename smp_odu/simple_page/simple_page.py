# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, url_for, current_app
from jinja2 import TemplateNotFound


simple_page = Blueprint('simple_page', __name__, static_folder='../../static',
                        template_folder= '../../templates')    #'/templates')
'''
@simple_page.route('/')
def rrr():
    return render_template('rem.html')
    return "Z"*33
'''

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    from run import app
    pname = '%s.html' % page
    print url_for('static', filename='CSS')
    # for k in current_app.config.keys():        print '%33s' % k, app.config.get(k)
    # return "Hello %s !" % pname
    try:
        templates = '%s/templates' % current_app.config.get('APP_ROOT')
        # simple_page['template_folder'] = templates
        print "ZZZ", pname, templates
        return render_template('rem.html', data=simple_page.root_path)  # pname)
    except TemplateNotFound:
        abort(404)

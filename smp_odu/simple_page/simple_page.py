# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, url_for, current_app, session, redirect, request, flash
from jinja2 import TemplateNotFound

import time, os

simple_page = Blueprint('simple_page', __name__,
                        template_folder= '../../templates')    #'/templates')
'''
@simple_page.route('/')
def rrr():
    return render_template('rem.html')
    return "Z"*33

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    from run import app
    pname = '%s.html' % page
    # print "simple_page.root_path", os.system("ls -l %s/*" % simple_page.static_folder)
    # for k in current_app.config.keys():        print '%33s' % k, app.config.get(k)
    # return "Hello %s !" % pname
    try:
        if session.get('logged_in'):
            return render_template('rem.html', data='index.html')
        else:
            return render_template('login.html', sdate=time.strftime("%d-%m-%Y %T", time.localtime(time.time())))
        templates = '%s/templates' % current_app.config.get('APP_ROOT')
        # simple_page['template_folder'] = templates
        print "ZZZ", pname, templates
        return render_template('rem.html', data=simple_page.root_path)  # pname)
    except TemplateNotFound:
        abort(404)
'''


from pylib import dbtools
import json

def	get_user(ulogin, password):
    if not (login and password):
        flash(u'Отсутствуют прльзователь login: %s  password: %s' % (ulogin, password))
    else:
        idb = dbtools.dbtools('host=212.193.103.21 dbname=b03 port=5432')
        if idb and idb.last_error:
            # print perse_res.ures(idb.last_error[:2])
            flash('%s %s' % (idb.last_error[0], str(idb.last_error[1]).decode('UTF-8')))
        elif idb:
            ulogin, password = ['6827', 'p6827']
            query = """SELECT u.disp, u.type, u.smena, u.subst, p.name, t.name AS tname FROM usr03 u
                JOIN person_sp p ON u.cod = p.cod JOIN sp_usrtype t ON u.type = t.cod WHERE login='%s' AND passwd='%s'""" % (ulogin, password)
            flash(query)
            ruser = idb.get_dict(query)
            if ruser:
                session['logged_in'] = True
                session['user'] = json.loads(json.dumps(ruser))
                return True
        else:
            flash("Not connect: ")
    return False

@simple_page.route('/logout')
def logout():
    session.pop('logged_in', None)
#	flash(u'Вы вышли из системы')	#'You were logged out')
    return redirect(url_for('simple_page.login'))
    # return render_template('login.html', sdate = time.strftime("%d-%m-%Y %T", time.localtime(time.time())))
	# return redirect(url_for('index'))


@simple_page.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    print "\tLogin:", request.form
    flash(str(request.form))
    flash(request.method)
    if request.method in ['POST', 'GET']:
        if get_user(request.form.get('ulogin'), request.form.get('password')):
            return redirect('show')
            # return render_template('test.html')
        
    return render_template('login.html', sdate = time.strftime("%d-%m-%Y %T", time.localtime(time.time())), error = error)


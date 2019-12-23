# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, session, request, flash
from werkzeug.local import LocalProxy

import time
import forms

main_page = Blueprint('main_page', __name__, template_folder= '../../templates')	#'/templates')

'''
	DELETE FROM calls WHERE nsbrg <3;
	DELETE FROM brignrd WHERE n_pst > 2;
	DELETE FROM bnaryd WHERE n_pst > 2;
	DELETE FROM sp_station WHERE cod > 2 AND cod <15;
	DELETE FROM usr03 WHERE subst > 2;
'''


def sout_row (row, **keywords):
	ss = []
	if not keywords:
		for s in row: ss.append(str(s))
	else:
		for k in keywords.keys():
			ss.append("%s: '%s'" % (k, keywords[k]))
	return '\t'.join(ss)
	

def get_data(tname, **keywords):
	""" Читать данные из БД "SELECT {*|<cols>} FROM <tname> [WHERE <where>] [<tail>];
	tname = <наименование таблицы (FROM ...)>
	keywords:
		cols = <наименование столбцов запрса (SELECT ...)>
		where = <условия (WHERE ...)>
		tail = [ORDER BY ... | LIMIT ... | ...]"""
	from run import get_db
	idb = LocalProxy(get_db)
	query = "SELECT * FROM vperson_sp WHERE n_pst IN (1,2)"
	rows = idb.get_rows(query)
	res = idb.get_table(tname)
	if not res:    return "Not data"
	ress = ["<pre>"]
	for r in res[1]:
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
			if ss and ss[0] == 'NEW_CALL':
				sajax.append("my_body| %s" % render_template('new_call.html'))
			if ss and ss[0] == 'KuKu':  sajax.append("my_body| %s" % render_template('test.html'))
			if ss and ss[0] == 'CLL_OPER':  sajax.append("my_body| %s" % get_data('call', swhere="t_done IS NULL"))
			return '~'.join(sajax)
			# return "~curr_dtime| %s ~events| %s" % (sdate, dict(request.form))
		return render_template('test.html')
	else:
		val = ('123', 'ZZZ')
		form = forms.PersonForm('values', disp=321, name=u'Иванов')
		return render_template('rem.html', form=form)

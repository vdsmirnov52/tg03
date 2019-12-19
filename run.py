#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Create an application instance."""
from smp_odu.app import create_app
from flask import g
from pylib import dbtools


# print help(create_app)
app = create_app()


def get_db ():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = dbtools.dbtools(app.config.get('DB_GSMP'))
	return db


@app.teardown_appcontext
def teardown_db (exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()


if __name__ == '__main__':
	app.run(host=app.config.get('APP_HOST'), port=app.config.get('APP_PORT'))

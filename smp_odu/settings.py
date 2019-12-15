# -*- coding: utf-8 -*-

import os
config = dict(
	APP_DIR = os.path.abspath(os.path.dirname(__file__)),  # This directory
	APP_ROOT = os.path.abspath(''),
	APP_HOST = '0.0.0.0',
	APP_PORT = None,    #50001,
	DATABASE=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'users.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	# PERMANENT_SESSION_LIFETIME=120,
	ULOGIN='admin',
	PASSWORD='123Admin',
	TITLE=u'Городец',
	# DB_GSMP='host=10.40.25.176 dbname=vms_ws port=5432 user=vms',
	# DB_GSMP='host=212.193.103.20 dbname=b03 port=5432 user=smirnov',
	DB_GSMP='host=127.0.0.1 dbname=b03 port=5432 user=smirnov',
)

# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask	#, render_template
#from smp_odu.constants import *
#from smp_odu import commands, public, user, services, call, patient
#from smp_odu.extensions import bcrypt, cache, csrf_protect, db, debug_toolbar, login_manager, migrate, webpack


def create_app(config_object='smp_odu.settings'):
	print "create_app", __name__
	"""An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

	:param config_object: The configuration object to use.
	"""
	app = Flask(__name__.split('.')[0])
	app.url_map.strict_slashes = False
	app.config.from_object(config_object)
#	register_extensions(app)
#	register_blueprints(app)
#	register_errorhandlers(app)
#	register_shellcontext(app)
#	register_commands(app)
	return app

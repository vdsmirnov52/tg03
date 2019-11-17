#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Create an application instance."""
from smp_odu.app import create_app

# print help(create_app)
app = create_app()

if __name__ == '__main__':
	app.run(host=app.config.get('APP_HOST'), port=app.config.get('APP_PORT'))

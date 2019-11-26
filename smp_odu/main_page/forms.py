# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FormField, TimeField, IntegerField, SelectField, TextField
from wtforms.validators import DataRequired, Required


class PersonForm(FlaskForm):
	vals = {}
	disp = IntegerField(u'Код:', default = vals.get('disp'), validators = [DataRequired()])
	code = StringField (u'Табельный №', validators = [DataRequired()], default = vals.get('name'))
	name = StringField(u'Фамилия И.О.:', validators = [DataRequired()])
	snils = StringField(u'СНИЛС:')
	type = SelectField(u'Тип', choices=((1, 'First'), (2, 'Second'), (4, 'ZZZ:'), (8, u'ФЫВА')))
	mdate = TimeField('Time')
	submit = SubmitField('submit')
	
	def __init__ (self, *args, **kwargs):
		"""Create instance."""
		if args:    print "args %s" % args, type(args)
		if kwargs:  print "kwargs %s" % kwargs
		super(PersonForm, self).__init__(*args, **kwargs)
		# self.user = None
		if args and args == 'values' and kwargs:
			self.vals = kwargs

class LoginForm(FlaskForm):
	disp = IntegerField(u'Код:', validators = [DataRequired()])
	login = StringField ('Login:', validators = [DataRequired()])
	passwd = PasswordField('Password:', validators = [DataRequired()])

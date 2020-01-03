# -*- coding: utf-8 -*-

#   Глобальный справочники
MENU_OO = [
	{'name': u'Принять вызов',	'type': [1, 2, 4, 8, 16],	'view': 'NEW_CALL', },
	{'name': u'Вызова в работе',	'type': [1, 2, 4, 8, 16],	'view': 'CLL_OPER',	},
	{'name': u'Архив вызовов',	'type': [1, 2, 4, 16],	'view': 'CLL_ARCH', 'opts': {}},
	{'name': u'Бригады',	'type': [1, 2, 4, 8, 16],	'view': 'BRG_WOKE', 'opts': {}},
	{'name': u'Машины',	'type': [1, 2, 4, 8, 16],   'view': 'AUTOS',	'opts': {}},
	{'name': u'Справка',	'type': [1, 2, 4],	'opts': {}},
	{'name': u'Статистика',	'type': [1, 2, 4],	'opts': {}},
]
call_colgroups = {
	'pkey':     ['cnumtotal'],
	'mark':     ['number', 'profile', 'reasn'],
	'addres':   ['street', 'house', 'korp', 'flat', 'pdzd', 'etj', 'pcod', 'phone'],
	'patient':  ['name', 'name2', 'age', 'sex'],
}

brig_colgroups = {
	'pkey': 'br_id',
	'mark': ['number', 'profile'],
}

#!/usr/bin/python -u
# -*- coding: utf-8 -*-

def     upper_ru (sinp):
	sdn =   u'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
	sup =   u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
	sout = []

	for c in unicode(sinp, "utf-8"):
		if c in sdn:
			sout.append (sup[sdn.index(c)])
		else:   sout.append (c)
	return  ''.join(sout).encode("utf-8")

if __name__ == "__main__":
	sss = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ 12345 !@#$%'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'\n"
	print sss, upper_ru(sss)

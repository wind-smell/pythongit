#!/usr/bin/env python
#-*- coding: utf-8 -*-

d = {'Michael':95, 
	'Bof':75,
	'Tracy':85}
print(d['Michael'])

d['Jack'] = 90

print(d['Jack'])
d.get('A')
d.get('A',-1)
if 'Tracy' in d:
	print('d')
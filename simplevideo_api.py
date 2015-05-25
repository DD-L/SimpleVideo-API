#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

class Tips:
	def __init__(self):
		self.message = 'Tips'
	def msg(self, message = ''):
		sys.stdout.write(message if message else self.message)

if __name__ == '__main__':
	message = '''

================================================
SimpleVideo-API:
  支撑SimpleVideo的音视频解析接口服务.
================================================

SimpleVideo-API 代码尚未从D-L.top中检出，请参见:
  * http://D-L.top 
  * https://github.com/DD-L/D-L.top.git
	

LICENSE
  copyright - Deel@d-l.top | d-l.top
------------------------------------------------

'''
	Tips().msg(message)
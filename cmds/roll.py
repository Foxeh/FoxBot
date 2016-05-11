import re,sys,unicodedata,time,math,httplib,urllib,random
import config

from functools import wraps
from interface import Interface
from symbol import parameters

class Roll(Interface):

	def _roll(self, data):
		res = 0
		regex = re.compile(r"^(?P<dice>\d*)d(?P<sides>\d+)((?P<sign>[+\-*/])(?P<modifier>\d+)+)?")
		match = regex.search(data.cmd['parameters']).groupdict()
		
		if match['dice'] is None:
			match['dice'] = "2";
		
		for i in xrange(int(match['dice'])):
			res += random.randint(1,int(match['sides']))
		
		print (res)
		
		return (data.usernick+" rolled a "+str(res), 0)

	def bang_roll(self, data):
		# !roll
		resp, err = self._roll(data)
		data.conn.msg(data.channel, resp)

	def dot_roll(self, data):
		# .roll
		pass

	def question_roll(self, data):
		# ?roll
		'''
			Returns help for the roll plugin.
		'''

		helpLines = (
			'Roll Help:',
			'	<!|.>roll <# of dice>d<# of sides> + <int>',
			'Example Roll: ',
			'	!roll 2d20+5',
			'Result:',
			'	( 14 + 6 ) + 5 = 25'
		)

		for line in helpLines:
			data.conn.msg(data.channel, line)
import re,sys,unicodedata,time,math,httplib,urllib
import config

from functools import wraps
from interface import Interface

class Roll(Interface):

	def roll(self, data):
		if not data.cmd["parameters"] or data.cmd["parameters"] == "help":
			data.conn.msg(foxdata.channel, "Try /roll 1d20+5")
			return

		print "test"

	def _slashroll(self, data):
		# /roll
		pass

	def _bangroll(self, data):
		# !roll
		pass

	def _dotroll(self, data):
		# .roll
		pass

	def _questionroll(self, data):
		# ?roll
		pass
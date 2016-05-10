import re,sys,unicodedata,time,math,httplib,urllib
import config

from functools import wraps
from interface import Interface

class Roll(Interface):

	def _roll(self, data):
		r = r"^(\d*)d(\d+)(([+-])(\d+)+)?" 

	def slash_roll(self, data):
		# /roll
		pass

	def bang_roll(self, data):
		# !roll
		pass

	def dot_roll(self, data):
		# .roll
		pass

	def question_roll(self, data):
		# ?roll
		pass
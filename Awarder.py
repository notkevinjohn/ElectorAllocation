#!/usr/bin/python3
import sys
from WinnerTakeAll import WinnerTakeAll
from Proportional import Proportional
from ProportionalTwoParty import ProportionalTwoParty

class Awarder():
	def __init__(self, awarder, config, data):
		self.awarder = awarder
		self.config = config
		self.data = data

	def award(self):
		exec("self.awarder = "+self.awarder+"()")
		results = self.awarder.award(self.data)
		return results

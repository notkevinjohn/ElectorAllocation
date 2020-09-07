#!/usr/bin/python3
import sys
from HuntingtonHill import HuntingtonHill
from HuntingtonHill_NoSenators import HuntingtonHill_NoSenators
from HuntingtonHill_OOP import HuntingtonHill_OOP
from DirectDemocracy import DirectDemocracy
from DemocracyQuotient import DemocracyQuotient
from Validator import Validator


class Allocator():
	def __init__(self, allocation, config, data):
		self.allocation = allocation
		self.config = config
		self.data = data

	def allocate(self):
		exec("self.allocator = "+self.allocation+"()")
		self.allocator.allocate(self.config['Electors'], self.data)
		validator = Validator()

		if not validator.validate(self.config['Electors'], self.data):
			raise Exception("Correct Number of Electors Not Allocated")

		dq = DemocracyQuotient().calc(self.data)
		return self.data, dq

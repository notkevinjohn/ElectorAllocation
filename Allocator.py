#!/usr/bin/python3
import sys
from HuntingtonHill import HuntingtonHill
from HuntingtonHill_NoSenators import HuntingtonHill_NoSenators
from HuntingtonHill_OOP import HuntingtonHill_OOP
from DirectDemocracy import DirectDemocracy
from DirectDemocracy_Senators import DirectDemocracy_Senators
from DemocracyQuotient import DemocracyQuotient
from Validator import Validator


class Allocator():
	def __init__(self, allocation, electors, data):
		self.allocation = allocation
		self.electors = electors
		self.data = data

	def allocate(self):
		exec("self.allocator = "+self.allocation+"()")
		self.allocator.allocate(self.electors, self.data)
		validator = Validator()

		if not validator.validate(self.electors, self.data):
			raise Exception("Correct Number of Electors Not Allocated")

		dq = DemocracyQuotient().calc(self.data)
		return self.data, dq

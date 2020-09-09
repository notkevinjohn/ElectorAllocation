#!/usr/bin/python3
import sys
from HuntingtonHill import HuntingtonHill
from HamiltonVinton import HamiltonVinton
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

		valid, allocated = validator.validate(self.electors, self.data)
		if not valid:
			raise Exception("Correct Number of Electors Not Allocated: "+str(allocated))

		dq = DemocracyQuotient().calc(self.data)
		return self.data, dq

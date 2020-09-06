#!/usr/bin/python3
import math
import time

class HuntingtonHill():

	initialElectors = 3

	def selectState(self):
		selectedState = None
		highestQ = 0
		for key in self.StateData:
			state = self.StateData[key]
			Q = self.quotient(state)
			if Q > highestQ:
				highestQ = Q
				selectedState = state
		return selectedState

	def quotient(self, state):
		return int(state['population']) / math.sqrt(state['electors'] * ( state['electors'] + 1))

	def allocate(self, Electors, StateData):
		self.Electors = int(Electors)
		self.StateData = StateData
		print (self.Electors)

		#Assign Initial Electors
		for key in self.StateData:
			state = self.StateData[key]
			state['electors'] = self.initialElectors
			self.Electors -= self.initialElectors

		print (self.Electors)

		#Assign population based Electors
		while self.Electors > 0:
			state = self.selectState()
			state['electors'] += 1
			self.Electors -= 1
			print (state['abbreviation'], state['electors'])
			time.sleep(1)



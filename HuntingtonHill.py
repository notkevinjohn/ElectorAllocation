#!/usr/bin/python3
import math

class HuntingtonHill():
	def selectState(self):
		selectedState = None
		highestQ = 0
		for state in self.States:
			stateCurrent = self.States[state]
			Q = self.quotient(stateCurrent)
			if Q > highestQ:
				highestQ = Q
				selectedState = stateCurrent
		return selectedState

	def quotient(self, state):
		return state['Population'] / math.sqrt(state['Seats'] * ( state['Seats'] + 1))

	def allocate(self, Seats, States):
		self.Seats = Seats
		self.States = States
		while self.Seats > 0:
			state = self.selectState()
			state['Seats'] += 1
			self.Seats -= 1
			if self.Seats == 0:
				break



#!/usr/bin/python3
import math

class HamiltonVinton():
	def allocate(self, Electors, StateData):
		USPopulation = 0
		Electors = int(Electors) - 102
		allocated = 0

		for key in StateData:
			state = StateData[key]
			USPopulation+=int(state['population'])
			state['electors']=2

		for key in StateData:
			state = StateData[key]
			popPercentage = int(state['population'])/USPopulation
			allocation = popPercentage * Electors
			allocation_round = round(allocation)
			remainder = allocation - allocation_round
			state['electors'] += allocation_round
			allocated += allocation_round
			state['remainder'] = remainder

		while allocated < Electors:
			state = self.largestRemainder(StateData)
			state['electors']+=1
			allocated+=1


	def largestRemainder(self, StateData):
		remainder = 0
		for key in StateData:
			state = StateData[key]
			if state['remainder'] > remainder:
				remainder = state['remainder']
				selectedState = state
			return selectedState

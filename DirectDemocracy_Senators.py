#!/usr/bin/python3
import math

class DirectDemocracy_Senators():
	def allocate(self, Electors, StateData):
		USPopulation = 0
		Electors = int(Electors) - 102
		for key in StateData:
			state = StateData[key]
			USPopulation+=int(state['population'])

		allocated = 0
		for key in StateData:
			state = StateData[key]
			popPercentage = int(state['population'])/USPopulation
			allocation = popPercentage * int(Electors)
			allocation_round = round(allocation)
			remainder = allocation - allocation_round
			state['electors'] = allocation_round
			allocated += allocation_round
			state['remainder'] = remainder

		while allocated < int(Electors):
			state = self.largestRemainder(StateData)
			state['electors']+=1
			allocated+=1


		#Assign Senators
		for key in StateData:
			state = StateData[key]
			state['electors']+=2
			allocated += 2

	def largestRemainder(self, StateData):
		remainder = 0
		for key in StateData:
			state = StateData[key]
			if state['remainder'] > remainder:
				remainder = state['remainder']
				selectedState = state
		return selectedState

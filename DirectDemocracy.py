#!/usr/bin/python3

class DirectDemocracy():
	def allocate(self, Seats, States):
		USPopulation = 0
		for state in States:
			USPopulation+=States[state]['Population']

		for state in States:
			selectedState = States[state]
			seats = int(round(selectedState['Population']/USPopulation * Seats))
			print (selectedState['Name'], selectedState['Population'], USPopulation, seats, Seats)
			selectedState['Seats']+= seats



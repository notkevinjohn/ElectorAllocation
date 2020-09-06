#!/usr/bin/python3

from HuntingtonHill import HuntingtonHill
from DirectDemocracy import DirectDemocracy
from ConfigLoader import ConfigLoader
from CSVLoader import CSVLoader

#Load Data
configLoader = ConfigLoader("Config.xml")
config = configLoader.config

csvLoader = CSVLoader("ElectionData.csv")
data = csvLoader.data

allocator = HuntingtonHill()
allocator.allocate(config['Electors'], data)

#for key in data:
#	state = data[key]
#	print (key, state['electors'])

#Add DC
#States['DC']={}
#States['DC']['Code'] = "DC"
#States['DC']['Name'] = "District of Columbia"
#States['DC']['Population'] = 572059
#States['DC']['Seats'] = 3
#States['DC']['Party'] = 'D'

#Add Senators
#for state in States:
#        States[state]['Seats'] += 2

#Calculate Totals
#DSeats = 0
#DPop = 0
#RSeats = 0
#RPop = 0
#for state in States:
#	stateData = States[state]
#	print (stateData)
#	if stateData['Party'] == 'D':
#		DSeats+=stateData['Seats']
#		DPop+=stateData['Population']
#
#	if stateData['Party'] == 'R':
#		RSeats+=stateData['Seats']
#		RPop+=stateData['Population']

#print()
#print ("Seats")
#print ("Republicans:", RSeats)
#print ("Democrats:", DSeats)
#print ("Total", RSeats + DSeats)

#print()
#print ("Population")
#print ("Republicans:", RPop)
#print ("Democrats:", DPop)
#print ("Total", RPop + DPop)

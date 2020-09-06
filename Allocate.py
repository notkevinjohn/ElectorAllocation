#!/usr/bin/python3

from HuntingtonHill import HuntingtonHill
from HuntingtonHill_NoSenators import HuntingtonHill_NoSenators
from DirectDemocracy import DirectDemocracy
from DemocracyQuotient import DemocracyQuotient
from ConfigLoader import ConfigLoader
from CSVLoader import CSVLoader
from Validator import Validator

#Load Data
configLoader = ConfigLoader("Config.xml")
config = configLoader.config

csvLoader = CSVLoader("ElectionData.csv")
data = csvLoader.data

allocator = DirectDemocracy()
allocator.allocate(config['Electors'], data)
validator = Validator()

if not validator.validate(config['Electors'], data):
	raise Exception("Correct Number of Electors Not Allocated")

for key in data:
	state = data[key]
	print (key, state['electors'])

dc = DemocracyQuotient().calc(data)
print(dc)

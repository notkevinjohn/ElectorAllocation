#!/usr/bin/python3

from HuntingtonHill import HuntingtonHill
from HuntingtonHill_NoSenators import HuntingtonHill_NoSenators
from DirectDemocracy import DirectDemocracy
from DemocracyQuotient import DemocracyQuotient
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

dc = DemocracyQuotient().calc(data)
print(dc)

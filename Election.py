import sys
from Allocator import Allocator
from Awarder import Awarder
#from ConfigLoader import ConfigLoader
from CSVLoader import CSVLoader
import time

class Election():
	def __init__(self, allocation, awarding, electors):
		self.allocation = allocation
		self.awarding = awarding
		self.electors = electors

		#configLoader = ConfigLoader("Config.xml")
		#self.config = configLoader.config

		csvLoader = CSVLoader("ElectionData.csv")
		self.data = csvLoader.data

	def elect(self):
		allocator = Allocator(self.allocation, self.electors, self.data)
		data, dq = allocator.allocate()

		awarder = Awarder(self.awarding, self.electors, self.data)
		votes_r, votes_d  = awarder.award()
		#for key in data:
		#	print (key, data[key]['electors'])
		print ('R:'+str(votes_r), 'D:'+str(votes_d), dq)

if __name__=="__main__":
	allocation = sys.argv[1].split(".")[0]
	awarding = sys.argv[2].split(".")[0]
	electors = sys.argv[3]
	election = Election(allocation, awarding, electors)
	election.elect()

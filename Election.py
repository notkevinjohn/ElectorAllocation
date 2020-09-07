import sys
from Allocator import Allocator
from Awarder import Awarder
from ConfigLoader import ConfigLoader
from CSVLoader import CSVLoader
import time

class Election():
	def __init__(self, allocation,awarding):
		self.allocation = allocation
		self.awarding = awarding

		configLoader = ConfigLoader("Config.xml")
		self.config = configLoader.config

		csvLoader = CSVLoader("ElectionData.csv")
		self.data = csvLoader.data

	def elect(self):
		allocator = Allocator(self.allocation, self.config, self.data)
		data, dq = allocator.allocate()

		awarder = Awarder(self.awarding, self.config, self.data)
		votes_r, votes_d  = awarder.award()
		print ('R:'+str(votes_r), 'D:'+str(votes_d))

if __name__=="__main__":
	allocation = sys.argv[1].split(".")[0]
	awarding = sys.argv[2].split(".")[0]
	election = Election(allocation, awarding)
	election.elect()

import sys
from Allocator import Allocator
from ConfigLoader import ConfigLoader
from CSVLoader import CSVLoader
import time

class Election():
	def __init__(self, allocation):
		self.allocation = allocation

		configLoader = ConfigLoader("Config.xml")
		self.config = configLoader.config

		csvLoader = CSVLoader("ElectionData.csv")
		self.data = csvLoader.data

	def elect(self):
		allocator = Allocator(self.allocation, self.config, self.data)
		data, dq = allocator.allocate()

		Votes_R = 0
		Votes_D = 0

		WinnerTakeAll = self.config['WinnerTakeAll'] == "True"
		if WinnerTakeAll:
			for key in data:
				state = data[key]
				Dem_Votes = float(state['DVotes'].strip("%"))
				Rep_Votes = float(state['RVotes'].strip("%"))
				if Dem_Votes > Rep_Votes:
					Votes_D += state['electors']
				if Rep_Votes > Dem_Votes:
					Votes_R += state['electors']

		else:
			for key in data:
				state =  data[key]
				Dem_Votes = float(state['DVotes'].strip("%"))/100
				Rep_Votes = float(state['RVotes'].strip("%"))/100
				electors = state['electors']
				allocated = 0

				Dem_Electors = Dem_Votes * electors
				Dem_Electors_Round = round(Dem_Electors)
				allocated += Dem_Electors_Round
				Dem_Electors_Rem = Dem_Electors - Dem_Electors_Round

				Rep_Electors = Rep_Votes * electors
				Rep_Electors_Round = round(Rep_Electors)
				allocated += Rep_Electors_Round
				Rep_Electors_Rem = Rep_Electors - Rep_Electors_Round

				Votes_R += Rep_Electors_Round
				Votes_D += Dem_Electors_Round

		print (Votes_R, Votes_D, Votes_R + Votes_D, dq)


if __name__=="__main__":
	allocation = sys.argv[1].split(".")[0]
	election = Election(allocation)
	election.elect()

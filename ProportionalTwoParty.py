import sys
from Allocator import Allocator
from ConfigLoader import ConfigLoader
from CSVLoader import CSVLoader
import time

class ProportionalTwoParty():
	def award(self, data):
		Votes_R = 0
		Votes_D = 0
		for key in data:
			state =  data[key]
			Dem_Votes = float(state['DVotes'].strip("%"))
			Rep_Votes = float(state['RVotes'].strip("%"))
			Sum_Votes = Dem_Votes+Rep_Votes
			Dem_Votes /= Sum_Votes
			Rep_Votes /= Sum_Votes
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

		return Votes_R, Votes_D



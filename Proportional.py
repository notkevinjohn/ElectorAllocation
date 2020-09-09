import sys
from Allocator import Allocator
from CSVLoader import CSVLoader
import time

class Proportional():
	def award(self, data):
		Votes_R = 0
		Votes_D = 0
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

		return Votes_R, Votes_D



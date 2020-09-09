import sys
from Allocator import Allocator
from CSVLoader import CSVLoader
import time

class WinnerTakeAll():
	def award(self, data):
		Votes_R = 0
		Votes_D = 0
		for key in data:
			state = data[key]
			Dem_Votes = float(state['DVotes'].strip("%"))
			Rep_Votes = float(state['RVotes'].strip("%"))
			if Dem_Votes > Rep_Votes:
				Votes_D += state['electors']
			if Rep_Votes > Dem_Votes:
				Votes_R += state['electors']
		return Votes_R, Votes_D



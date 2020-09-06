import sys

class DemocracyQuotient():
	def calc(self, data):
		maxPop = 0
		minPop = sys.maxsize
		for key in data:
			state = data[key]
			if int(state['population']) > maxPop:
				maxPop = int(state['population'])
				maxPopState = state
			if int(state['population']) < minPop:
				minPop = int(state['population'])
				minPopState = state

		maxStatePop = int(maxPopState['population'])
		minStatePop = int(minPopState['population'])
		maxStateElectors = int(maxPopState['electors'])
		minStateElectors = int(minPopState['electors'])
		quotientMin = (minStateElectors/minStatePop)
		quotientMax = (maxStateElectors/maxStatePop)
		print (quotientMin, quotientMax)
		return quotientMin/quotientMax

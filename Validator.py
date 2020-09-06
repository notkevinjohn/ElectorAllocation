class Validator():
	def validate(self, Electors, StateData):
		allocated = 0
		for key in StateData:
			state = StateData[key]
			allocated += float(state['electors'])
		print(allocated)
		return  int(Electors) == allocated

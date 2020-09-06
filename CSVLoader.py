class CSVLoader():
	data = {}
	def __init__(self, dataFile):
		with open(dataFile) as data:
			for line in data:
				dataLine = (line.strip().split(","))
				name = dataLine[0]
				abbreviation = dataLine[1]
				population = dataLine[2]
				DVotes = dataLine[3]
				RVotes = dataLine[4]

				self.data[name] = {}
				self.data[name]['abbreviation'] = abbreviation
				self.data[name]['population'] = population
				self.data[name]['DVotes'] = DVotes
				self.data[name]['RVotes'] = RVotes

if __name__ == "__main__":
	loader = CSVLoader("ElectionData.csv")
	data = loader.data
	for item in data:
		print (item, data[item])

import json

StateData = {}
with open("") as states:
	for line in states:
		data = line.strip().split("-")
		name = data[0].strip()
		code = data[1].strip()
		StateData[code]={}
		StateData[code]['Name'] = name

with open("states.json","w+") as outfile:
	json.dump(StateData, outfile)

#!/usr/bin/python3
import json
import geopandas as gpd
import matplotlib.pyplot as plt

States = {}
Seats = 538

def selectState():
	selectedState = None
	highestHHQ = 0
	for state in States:
		stateSelected = States[state]
		if stateSelected['A'] > highestHHQ:
			highestHHQ = stateSelected['A']
			selectedState = stateSelected
	return selectedState

def calculateHHQ(state):
	return state['Population'] / pow(state['Seats'] *( state['Seats'] + 1), 1/2)

with open("data.csv") as data:
	for item in data:
		stateData = item.strip().split(",")
		Name = stateData[0].strip()
		Code = stateData[1].strip()
		Population = stateData[2].strip()
		States[Code]={}
		States[Code]['Name'] = Name
		States[Code]['Population'] = int(Population)
		States[Code]['Seats'] = 1
		Seats -= 1
		States[Code]['A'] = int(Population)

while Seats > 48:
	state = selectState()
	state['A'] = int(calculateHHQ(state))
	state['Seats'] += 1
	Seats -= 1
	if Seats == 0:
		break
#map_df = gpd.read_file("shapefiles/cb_2018_us_state_500k.shp")

map_df = gpd.read_file("shapefiles/states.shp")
f, ax = plt.subplots(1, figsize=(6, 6))
ax = map_df.plot(ax=ax)
ax.set_axis_off()
plt.savefig("Map.png", dpi=1200)

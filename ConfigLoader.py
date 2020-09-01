import xml.etree.ElementTree as ET
import sys

class ConfigLoader():
	tags = ['Electors','WinnerTakeAll']
	def __init__(self, configFile):
		self.config = {}
		tree = ET.parse(configFile)
		root = tree.getroot()
		for child in root:
			if child.tag in self.tags:
				self.config[child.tag] = child.text


if __name__ == "__main__":
	cl = ConfigLoader("Config.xml")
	print (cl.config)

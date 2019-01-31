# Project: contentDM_Statistics.py
# Organization: Southern Illinois University Edwardsville, Lovejoy Library
# Team: Digital Initiatives
# Programmer: Jacob Grubb (jagrubb@siue.edu)
# File:  contentDM_Statistics.py

#Dependencies
import json
import csv
#import requests

collection_list = []
#Look for external file containing contentDM collection list
with open("./collection_list.json", 'r') as jsonReader:
  collection_list = json.load(jsonReader)

for item in collection_list:
	print item
#Attempt to connect to contentDM server

#Get username, password for contentDM domain

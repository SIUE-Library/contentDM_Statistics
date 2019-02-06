# Project: contentDM_Statistics.py
# Organization: Southern Illinois University Edwardsville, Lovejoy Library
# Team: Digital Initiatives
# Programmer: Jacob Grubb (jagrubb@siue.edu)
# File:  contentDM_Statistics.py

#Dependencies
import json
import csv
#import requests
from getpass import getpass

collection_list = []
#Look for external file containing contentDM collection list
with open("./collection_list.json", 'r') as jsonReader:
  collection_list = json.load(jsonReader)

for item in collection_list:
	print item
#Attempt to connect to contentDM server

#Get username, password for contentDM domain
user_name = input("Please enter CONTENTdm user name: ")
user_pass = getpass("Password: ")

#Get dates to draw reports:
start_date = input("Please input start date to draw reports from (YYYYMM): ")
end_date = input("Please input end date to draw reports from (YYYYMM): ")

url = "https://collections.carli.illinois.edu:8443/cdm4/admin/admin_jscripts/admin_reports_pageviews_export.php?CISOROOT=/{0}&CISODATE={1}"
#url{0} =: variable name of the collection, from collection_list.json
#url{1} =: date to draw report, in form of YYYYMM

# end - start => 201812 - 201605 = 000207
# 
#
#
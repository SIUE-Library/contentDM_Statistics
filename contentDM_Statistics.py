# Project: contentDM_Statistics.py
# Organization: Southern Illinois University Edwardsville, Lovejoy Library
# Team: Digital Initiatives
# Programmer: Jacob Grubb (jagrubb@siue.edu)
# File:  contentDM_Statistics.py

#Dependencies
import json
import csv
import time
import requests
import os
from getpass import getpass

#Get username, password for contentDM domain
user_name = input("Please enter CONTENTdm user name: ")
user_pass = getpass("Password: ")

#Get dates to draw reports:
start_date = input("Please input start date to draw reports from (YYYYMM): ")
end_date = input("Please input end date to draw reports from (YYYYMM): ")

def getReports(user_name, user_pass, start_date, end_date):
  #Attempt to connect to contentDM server
  url = "https://collections.carli.illinois.edu:8443/cdm4/admin/admin_jscripts/admin_reports_pageviews_export.php?CISOROOT=/{0}&CISODATE={1}"
  #url{0} =: variable name of the collection, from collection_list.json
  #url{1} =: date to draw report, in form of YYYYMM
  collection_list = []
  #Look for external file containing contentDM collection list
  with open("./test_collection_list.json", 'r') as jsonReader:
    collection_list = json.load(jsonReader)
  # end - start => 201812 - 201605 = 000207
  # start_date[0:3] => 2016
  year_difference = int(end_date[0:4]) - int(start_date[0:4])
  year_to_months = year_difference * 12
  # end_date[0:3] => 2018
  # _SUBTRACT_ => 2
  # _MULTIPLY_ => 2 X 12 = 24
  month_difference =  int(end_date[4:6]) - int(start_date[4:6])
  # start_date[4:6] => 05
  # end_date[4:6] => 12
  # _SUBTRACT_ => 7
  # _ADD_ => 24 + 7 = 31
  total_months = year_to_months + month_difference
  # Total of 31 Months

  # Get list of months to take
  # Start_date  = 201605
  # Start_date + 1 = 201606
  # Start_date + 5 = 201610

  list_of_dates = []
  current_date = start_date
  while(current_date <= end_date):
    list_of_dates.append(current_date)
    if(int(current_date[4:6]) + 1 > 12):
      new_year = int(current_date[0:4]) + 1
      current_date = str(new_year) + "01"
    else:
      current_date = str(int(current_date) + 1)
    pass

  list_of_urls = []
  for coll_text in collection_list:
    for date_text in list_of_dates:
      list_of_urls.append(url.format(coll_text, date_text))
  with requests.Session() as session:
    payload = {
      'username': user_name,
      'pass': user_pass
    }
    post = session.post(list_of_urls[0], data=payload)
    for url in list_of_urls:
      try:
        server_response = session.get(url, data=payload)
        #server_response = url
        print(server_response.content)
        time.sleep(0.1)
      except ConnectionError:
        print("There was a connection error trying to get: " + url)
      except:
        print("There was an error trying to get: " + url)

def parseReports(reports_dir, target_file):

  return True


getReports(user_name, user_pass, start_date, end_date):
parseReports("./reports/", "./")
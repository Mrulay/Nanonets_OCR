# -*- coding: utf-8 -*-
"""ocr_using_nanonets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HWaaAce-Js756lmyYCWSCW6-p72w6aI2

# Creating the model
"""

import requests, os, json

  
url = "https://app.nanonets.com/api/v2/ObjectDetection/Model/"
api_key = "GO-dODr6ztfVeAftR5tBQ86YrDUhJvsj"

##
payload = "{\"categories\" : [\"number_plate\"], \"model_type\": \"ocr\"}"
headers = {'Content-Type': "application/json",}

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(api_key, ''), data=payload)
model_id = json.loads(response.text)["model_id"]

print(response.text)

"""# Checking the model status"""

url = "https://app.nanonets.com/api/v2/ObjectDetection/Model/1bd47ff4-ef5c-4ca8-aded-714bf922e19e"

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(api_key,''))

state = json.loads(response.text)["state"]
status = json.loads(response.text)["status"]

if state != 5:
	print("The model isn't ready yet, it's status is:", status)
else:
	print("NEXT RUN: python ./code/prediction.py ./images/151.jpg")
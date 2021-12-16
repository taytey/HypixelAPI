import requests
import json
from pprint import pprint

#Function with an argument 'call' that grabs 'name_link' and inputs and gets the info via the url in the variable 'name_link'
def getInfo(call):
    r = requests.get(call)
    return r.json()

#Variable that stores name on input
name = input()

#Search by UUID; Not implemented yet
uuid = 'f5d767ffb1ae4ea19c8cf683ef52e05e'
uuid_dashed = 'f5d767ff-b1ae-4ea1-9c8c-f683ef52e05e'

#API Key accesses Hypixel's API and allows data to be pulled in
API_KEY = "3c29eae3-03d6-4a40-a3f8-aca3d8931fa7"

#Hypixel API JSON files
name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid_dashed}"


#Print data from chosen name that we set in the 'name' variable above
print(getInfo(name_link))


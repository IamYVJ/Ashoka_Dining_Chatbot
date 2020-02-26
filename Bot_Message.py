import sys
import re
import json
from datetime import date 
# from pathlib import Path, PureWindowsPath

def getJSON():
    # filename = PureWindowsPath("output.json")
    # correct_path = Path(filename) # Convert path to the right format for the current operating system

    dining_menu = open("new.json")
    dining_menu = json.load(dining_menu)
    return(dining_menu)
    
def getMeal(n):
    today = date.today()
    print('_' + today.strftime("%A, %d %B %Y") + '_')
    data = getJSON()
    print()
    print('*' + n.title() + ':*')
    print(data["dining_menu"][today.weekday()][0][n].title())
    
def searchMsg():

    query = str(sys.argv[1]).lower()

    if re.search("breakfast", query)!=None:
        getMeal("breakfast")
    elif re.search("lunch", query)!=None:
        getMeal("lunch")
    elif re.search("snacks", query)!=None:
        getMeal("snacks")
    elif re.search("dinner", query)!=None:
        getMeal("dinner")

# print(getJSON())
# getMeal("snacks")
searchMsg()
import re
import json
# from pathlib import Path, PureWindowsPath

def getJSON():
    # filename = PureWindowsPath("output.json")
    # correct_path = Path(filename) # Convert path to the right format for the current operating system

    dining_menu = open("output.json")
    dining_menu = json.load(dining_menu)
    return(dining_menu[0]["data"])

def getData(data):
    ss = str(data)
    p1 = ss.find("text")
    ss = ss[p1+8:-2]
    ss = ss.replace('\\r', '\n')
    ss = ss.replace(',', '')
    print(ss)
    print(ss.find('\''))
    ss = ss.replace('\'', '\"')
    return ss

data = getJSON()
day = []
for i in range(4,11):
    data1 = [{"breakfast": getData(data[i][1]),
            "lunch":getData(data[i][2]),
            "snacks":getData(data[i][3]),
            "dinner":getData(data[i][4])}]
    day.append(data1)
day = {"dining_menu" : day}

with open('new1.json','w+') as new:
    new.write(json.dumps(day))

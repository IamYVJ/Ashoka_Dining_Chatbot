import sys
import re
import json
from datetime import date, datetime
# from pathlib import Path, PureWindowsPath

def getJSON(s):
    # filename = PureWindowsPath("output.json")
    # correct_path = Path(filename) # Convert path to the right format for the current operating system

    dining_menu = open(s)
    dining_menu = json.load(dining_menu)
    return(dining_menu)
    
def getMeal(n):
    today = date.today()
    print('_' + today.strftime("%A, %d %B %Y") + '_')
    data = getJSON("new.json")
    print("")
    print('*' + n.title() + ':*')
    print(data["dining_menu"][today.weekday()][0][n].title())
    
def getNextShuttle():
    today = datetime.today()
    print('_' + today.strftime("%A, %d %B %Y, %H:%M") + '_')
    weekday = "Weekdays"
    if today.weekday()>4:
        weekday = "Weekends"
    hour = int(today.strftime("%H"))
    mint = int(today.strftime("%M"))
    data = getJSON("DELHI_Shuttle_Schedule.json")
    print("")
    print('*Campus To Metro:*')
    i = 0
    while i<27:
        if int(data[weekday]["C2M"][i][:2])>=hour:
            break
        i+=1
    while int(data[weekday]["C2M"][i][:2])==hour:
        if int(data[weekday]["C2M"][i][3:])>=mint:
            break
        i+=1
    while i<27:
        print(data[weekday]["C2M"][i])
        i+=1
    print("")
    print('*Metro To Campus:*')
    i = 0
    while i<27:
        if int(data[weekday]["M2C"][i][:2])>=hour:
            break
        i+=1
    while int(data[weekday]["M2C"][i][:2])==hour:
        if int(data[weekday]["M2C"][i][3:])>=mint:
            break
        i+=1
    while i<27:
        print(data[weekday]["M2C"][i])
        i+=1

def getShuttle():
    today = datetime.today()
    print('_' + today.strftime("%A, %d %B %Y, %H:%M") + '_')
    weekday = "Weekdays"
    if today.weekday()>4:
        weekday = "Weekends"
    print("")
    print("```" + weekday + " Schedule```")
    data = getJSON("DELHI_Shuttle_Schedule.json")
    print("")
    print('*Campus To Metro:*')
    i = 0
    while i<27:
        print(data[weekday]["C2M"][i])
        i+=1
    print("")
    print('*Metro To Campus:*')
    i = 0
    while i<27:
        print(data[weekday]["M2C"][i])
        i+=1

def getNumber(n):
    data = getJSON("Numbers.json")
    print("")
    print('*' + n + ':*')
    for i in data[n]:
        print("_" + str(i) + "_: " + data[n][i])

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
    elif re.search("shuttle", query)!=None:
        if re.search("next", query)!=None:
            getNextShuttle()
        elif re.search("full", query)!=None or re.search("all", query)!=None:
            getShuttle()
        else:
            getNextShuttle()
    elif re.search("security", query)!=None:
        getNumber("Security")
    elif re.search("admin", query)!=None:
        getNumber("Admin Help-Desk")
    elif re.search("it help", query)!=None:
        getNumber("IT Help-Desk")
    elif re.search("infirmary", query)!=None:
        getNumber("Infirmary")
    elif re.search("maintenance", query)!=None:
        getNumber("Maintenance")
    elif re.search("housekeeping", query)!=None:
        getNumber("Housekeeping")
    elif re.search("transport", query)!=None:
        getNumber("Transport")
    elif re.search("dhaba", query)!=None:
        getNumber("Dhaba")
    elif re.search("rasaananda", query)!=None:
        getNumber("Rasaananda")
    elif re.search("hunger cycle", query)!=None or re.search("thc", query)!=None:
        getNumber("The Hunger Cycle")
    elif re.search("dosai", query)!=None:
        getNumber("Dosai")
    elif re.search("pizza", query)!=None:
        getNumber("Chicago Pizza")
    elif re.search("amul", query)!=None:
        getNumber("Amul")
# print(getJSON())
# getMeal("snacks")
# getNextShuttle()
# getShuttle()
# getNumber("Security")
searchMsg()
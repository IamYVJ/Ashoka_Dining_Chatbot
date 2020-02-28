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
            # while i<27:
            #     if int(data[weekday]["C2M"][i][3:])>=mint:
            #         break
            #     i+=1
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
            # while i<27:
            #     if int(data[weekday]["M2C"][i][3:])>=mint:
            #         break
            #     i+=1
            break
        i+=1
    while int(data[weekday]["M2C"][i][:2])==hour:
        if int(data[weekday]["M2C"][i][3:])>=mint:
            break
        i+=1
    while i<27:
        print(data[weekday]["M2C"][i])
        i+=1

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
        else:
            getNextShuttle()
# print(getJSON())
# getMeal("snacks")
getNextShuttle()
# searchMsg()
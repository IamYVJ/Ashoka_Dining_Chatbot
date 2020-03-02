import sys
import re
import json
import datetime
# from pathlib import Path, PureWindowsPath

def getJSON(s):
    # filename = PureWindowsPath("output.json")
    # correct_path = Path(filename) # Convert path to the right format for the current operating system

    dining_menu = open(s)
    dining_menu = json.load(dining_menu)
    return(dining_menu)
    
def getFoodOutlets():
    data = getJSON("Food_Outlets.json") 
    print('*Food Outlets:*')
    print("")
    for i in data:
        print('_'+str(i).title()+'_')  

def getTKS():
    today = datetime.datetime.today()
    print('_' + today.strftime("%A, %d %B %Y") + '_')
    data = getJSON("TKS_Menu.json")
    print("")   
    print('*TKS Menu:*')
    print("-----------------------")
    for i in data:
        print('_'+str(i).title()+'_')
        for j in data[i]:
            print(str(j).title())
        print("-----------------------")

def getDayMeal(m, d):
    today = datetime.datetime.today() + datetime.timedelta(days=d)
    print('_' + today.strftime("%A, %d %B %Y") + '_')
    data = getJSON("new.json")
    print("")   
    print('*' + m.title() + '*', end = "")
    if m=='breakfast':
        print(" _(08:00-10:30)_:")
    elif m=='lunch':
        print(" _(12:30-14:30)_:")
    elif m=='snacks':
        print(" _(16:45-18:15)_:")
    elif m=='dinner':
        print(" _(19:30-22:30)_:")
    else:
        print(":")
    print(data["dining_menu"][today.weekday()][0][m].title())

def getMeal(m):
    today = datetime.datetime.today()
    hour = int(today.strftime("%H"))
    if (m=="breakfast" and hour>=11) or (m=="lunch" and hour>=15) or (m=="snacks" and hour>=19) or (m=="dinner" and hour>=23):
            today = today + datetime.timedelta(days=1)
    print('_' + today.strftime("%A, %d %B %Y") + '_')
    data = getJSON("new.json")
    print("")
    print('*' + m.title() + '*', end = "")
    if m=='breakfast':
        print(" _(08:00-10:30)_:")
    elif m=='lunch':
        print(" _(12:30-14:30)_:")
    elif m=='snacks':
        print(" _(16:45-18:15)_:")
    elif m=='dinner':
        print(" _(19:30-22:30)_:")
    else:
        print(":")
    print(data["dining_menu"][today.weekday()][0][m].title())
    
def getNextShuttle():
    today = datetime.datetime.today()
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
    if i==27:
        print("Sorry! No more shuttles scheduled for today!")
    else:
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
    if i==27:
        print("Sorry! No more shuttles scheduled for today!")
    else:
        while i<27:
            print(data[weekday]["M2C"][i])
            i+=1

def getShuttle():
    today = datetime.datetime.today()
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

def getHelp():
    with open("Help.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i)
        file.close()

def getAbout():
    with open("About.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i)
        file.close()

def searchMsg():

    query = str(sys.argv[1]).lower()

    if query=="help":
        getHelp()
    elif re.search("about", query)!=None:
        getAbout()

    elif re.search("breakfast", query)!=None:
        if re.search("tomorrow", query)!=None or re.search("kal", query)!=None:
            getDayMeal("breakfast", 1)
        elif re.search("yesterday", query)!=None:
            getDayMeal("breakfast", -1)
        else:
            getMeal("breakfast")
    elif re.search("lunch", query)!=None:
        if re.search("tomorrow", query)!=None or re.search("kal", query)!=None:
            getDayMeal("lunch", 1)
        elif re.search("yesterday", query)!=None:
            getDayMeal("lunch", -1)
        else:
            getMeal("lunch")
    elif re.search("snacks", query)!=None:
        if re.search("tomorrow", query)!=None or re.search("kal", query)!=None:
            getDayMeal("snacks", 1)
        elif re.search("yesterday", query)!=None:
            getDayMeal("snacks", -1)
        else:
            getMeal("snacks")
    elif re.search("dinner", query)!=None:
        if re.search("tomorrow", query)!=None or re.search("kal", query)!=None:
            getDayMeal("dinner", 1)
        elif re.search("yesterday", query)!=None:
            getDayMeal("dinner", -1)
        else:
            getMeal("dinner")

    elif re.search("tks", query)!=None or re.search("kitchen stories", query)!=None:
        getTKS()

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

    elif re.search("food outlet", query)!=None:
        getFoodOutlets()

    elif re.search("hi", query)!=None or re.search("hey", query)!=None or re.search("hello", query)!=None:
        print("Hey! Hope you are having a great day.")
        print("Type _Help_ for the available list of Commamnds")
    else:
        print("Sorry, Invalid Input! Type _Help_ for the available list of Commamnds")
# print(getJSON())
# getMeal("snacks")
# getNextShuttle()
# getShuttle()
# getNumber("Security")
# getHelp()
# getTKS()
searchMsg()
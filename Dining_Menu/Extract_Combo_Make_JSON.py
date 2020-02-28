import tabula
import json

# Read pdf into DataFrame
df = tabula.read_pdf("Dining_Menu\Combo_Menu.pdf", pages='all')
# print(df[0])
# print(type(df[0]))
# print(df[0].iloc[0])

#first row data
data = [["SOUTH INDIAN COMBOS"]]
data.extend(df[0].values.tolist())
# print(data)
combo_menu = {
    "SOUTH INDIAN COMBOS" : [],
    "CHINESE COMBOS" : [],
    "CONTINENTAL COMBOS" : [],
    "NORTH INDIAN COMBOS" : []
}
combo = "SOUTH INDIAN COMBOS"
for i in range(len(data)):
    if data[i][0]=="SOUTH INDIAN COMBOS":
        combo = "SOUTH INDIAN COMBOS"
    elif data[i][0]=="CONTINENTAL COMBOS":
        combo = "CONTINENTAL COMBOS"
    elif data[i][0]=="CHINESE COMBOS":
        combo = "CHINESE COMBOS"
    elif data[i][0]=="NORTH INDIAN COMBOS":
        combo = "NORTH INDIAN COMBOS"
    else:
        combo_menu[combo].append(data[i][0])

# print(combo_menu)

with open("TKS_Menu.json", "w") as file:
    file.write(json.dumps(combo_menu))
    file.close()
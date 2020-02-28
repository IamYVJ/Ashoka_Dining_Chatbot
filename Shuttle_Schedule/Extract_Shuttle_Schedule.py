from openpyxl import load_workbook

workbook = load_workbook(filename="Shuttle_Schedule\DELHI_Shuttle_Schedule.xlsx")
sheet = workbook.active
# print(sheet)
for row in sheet.rows:
    for column in row:
        print(column.value)

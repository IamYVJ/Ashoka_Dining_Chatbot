import tabula

# Read pdf into DataFrame
df = tabula.read_pdf("Dining_Menu\Menu.pdf", pages='all')
# print(df)
tabula.convert_into("Dining_Menu\Menu.pdf", "Dining_Menu\output.json", output_format="json", pages='all')

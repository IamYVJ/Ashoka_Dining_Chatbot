from tika import parser

raw = parser.from_file('Dining_Menu\Menu.pdf')
print(raw['content'])
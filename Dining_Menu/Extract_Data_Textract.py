import textract

# text = textract.process("Dining_Menu\Menu.pdf")

# print(text)

#Not working

text = textract.process("Dining_Menu\Menu.pdf", method='tesseract', language='eng')
print(text)

#Not Working
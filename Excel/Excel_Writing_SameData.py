import openpyxl

# Writing Same Data
file = '/data1.xlsx'
workbook = openpyxl.load_workbook(file)  # load the workbook
sheet = workbook.active
# workbook.active (In case to write in the current sheet

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(r, c).value = "Hello"

workbook.save(file)

import gspread
import pprint

gc = gspread.service_account()
# Alternate: gc = gspread.service_account(filename='path/to/the/downloaded/file.json')


sh = gc.open("Frank Expenses")




print(sh.sheet1.get('A1:J61'))

worksheet = sh.worksheet("Test Sheet")1
numRows = worksheet.row_count

print(numRows)
worksheet.format('A1:J1', {'textFormat': {'bold': True}})
worksheet.update('A70:J130', sh.sheet1.get('A1:J61'))

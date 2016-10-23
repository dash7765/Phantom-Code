import xlrd

workbook = xlrd.open_workbook('Client Datasheet.csv')
worksheet = workbook.sheet_by_name('Client Datasheet')
num_rows = worksheet.nrows - 1
curr_row = -1
while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        print (row)
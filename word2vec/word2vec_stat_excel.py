import xlrd
import sys

current_row = 0
sheet_num = 1
input_total = 0
output_total = 0


COUNT_STAT = False
UNKNOWN = True
stat = { i: 0 for i in range(1, 11)}

# path to the file you want to extract data from
src = sys.argv[1]

book = xlrd.open_workbook(src)

# select the sheet that the data resids in
work_sheet = book.sheet_by_index(0)

# get the total number of rows
num_rows = work_sheet.nrows - 1

while current_row < num_rows:
    input_total = ""
    row_header = work_sheet.cell_value(current_row, 0)
    if not UNKNOWN:
        coef = work_sheet.cell_value(current_row, 2)
    else:
        coef = ""
    input_total = str(row_header) + " " +str(work_sheet.cell_value(current_row, 1)) + " " + str(coef)
    current_row += 1
    print(input_total)

    if COUNT_STAT:
        for i in range(1, 11):
            if coef*10 <= i and coef*10 >= i-1:
                stat[i] += 1
                break
if COUNT_STAT:
    print(stat)

#print(num_rows)

import os
import csv
import xlsxwriter

def csv_write_table(path, name, content1, content2, start_row=4):

    words1 = [l[0].lower() for l in content1]
    words2 = [l[0].lower() for l in content2]

    out_path = os.path.join(path, name + ".csv")
    
    workbook = xlsxwriter.Workbook(out_path + '.xlsx')

    book_format = workbook.add_format(properties={'bold': True, 'font_color': 'red'})
    worksheet = workbook.add_worksheet('Pars')
    
    worksheet.write(start_row, 0, "word")
    worksheet.write(start_row, 1, "freq")
    worksheet.write(start_row, 2, "log")
    worksheet.write(start_row, 4, "word")
    worksheet.write(start_row, 5, "freq")
    worksheet.write(start_row, 6, "log")
    
    
    rows = start_row + 1
    for line in content1:
        word, freq, log = line
        if word.lower() in words2:
            worksheet.write(rows, 0, word.lower(), book_format)
        else:
            worksheet.write(rows, 0, word.lower())
        worksheet.write(rows, 1, freq)
        worksheet.write(rows, 2, log)
        rows += 1
        
    rows = start_row + 1
    for line in content2:
        word, freq, log = line
        if word.lower() in words1:
            worksheet.write(rows, 4, word.lower(), book_format)
        else:
            worksheet.write(rows, 4, word.lower())
        worksheet.write(rows, 5, freq)
        worksheet.write(rows, 6, log)
        rows += 1
    workbook.close()


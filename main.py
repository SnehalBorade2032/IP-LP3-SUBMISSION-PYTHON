
import csv

tab_in = csv.reader(open('EQ010114.tsv'), dialect=csv.excel_tab)
comma_out = csv.writer(open('EQ10114.csv', 'w'), dialect=csv.excel)

for row in tab_in:
    comma_out.writerow(row)

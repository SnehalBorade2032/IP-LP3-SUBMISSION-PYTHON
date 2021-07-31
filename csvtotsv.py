import csv
with open('EQ010114.csv', 'r') as csv_in, open('csv_to_tsv_output.tsv', 'w') as tsv_out:
    csv_in = csv.reader(csv_in)
    tsv_out = csv.writer(tsv_out, delimiter='\t')

    for row in csv_in:
        tsv_out.writerow(row)
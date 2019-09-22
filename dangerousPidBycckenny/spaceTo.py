import csv
with open('permission_matrix_malicious_zhou1.csv', newline='') as infile, open('outfiles1.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=' ')
    writer = csv.writer(outfile, delimiter=',')
    for row in reader:
        row.append('1')
        writer.writerow(row)
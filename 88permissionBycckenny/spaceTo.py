import csv
with open('permission_mapping1.csv', newline='') as infile, open('mapping.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='\n')
    writer = csv.writer(outfile, delimiter=',')
    for row in reader:
        #row.append('1')
        writer.writerow(row)
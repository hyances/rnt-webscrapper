import csv

input = open('rtn_colombia.csv', 'rb')
output = open('rtn_colombia_cleaned.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if any(field.strip() for field in row):
        writer.writerow(row)
input.close()
output.close()

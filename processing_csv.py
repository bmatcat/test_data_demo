import csv

with open('MOCK_DATA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[1]} {row[2]} ,with email address {row[3]} is a {row[4]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
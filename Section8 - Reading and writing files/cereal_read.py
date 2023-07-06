import csv

csv_filename = 'Section8 - Reading and writing files\cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
import csv
import os.path
import pandas as pd

'''
Processing a csv file, changing delimiter to ',' and reformat data with 'strip()'
'''

def convert_csv_format(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        rows = list(reader)


    with open(output_file, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        for row in rows:
            formatted_row = []
            for item in row:
                try:
                    formatted_item = float(item.replace(',', '.'))
                except ValueError:
                    formatted_item = item.strip('"')
                formatted_row.append(formatted_item)
            writer.writerow(formatted_row)

    print(f"Conversion completed.")


indir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(indir, '../01_DATA/Z13/Z13 Datensammlung.csv')
output_file = os.path.join(indir, '../01_DATA/Z13/Z13_Datensammlung_Processed.csv')
convert_csv_format(input_file, output_file)
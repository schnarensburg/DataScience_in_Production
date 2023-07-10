import csv
import os.path
import re

'''
Sorting the results and formatting for further analysis
'''

def sort_csv(file_path):
    # Read the CSV file and load its contents into a list
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)[1:]

    # Sort the data rows based on the first entry (numbers after the plus sign)
    sorted_rows = sorted(rows, key=lambda x: x[0])

    # Write the sorted rows back to the CSV file
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(sorted_rows)


# Example usage
in_dir = os.path.dirname(__file__)
file_path = os.path.join(in_dir, "../../10_RESULTS/3D_Analysis/z13_tooth_deviation.csv")
sort_csv(file_path)

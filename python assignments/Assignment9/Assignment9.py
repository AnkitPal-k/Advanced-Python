import csv
import json

input_file = "python assignments/Assignment9/input.csv"
output_file = "python assignments/Assignment9/output.json"

# Read data from CSV file
with open(input_file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Convert CSV data to JSON and write to output file
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")
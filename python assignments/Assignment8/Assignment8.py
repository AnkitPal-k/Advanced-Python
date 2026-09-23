input_file = "python assignments/Assignment8/input.txt"
output_file = "python assignments/Assignment8/output.txt"

# Read the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Count lines
line_count = len(lines)
print("Total number of lines:", line_count)

# Extract first two lines
first_two_lines = lines[:2]

# Write first two lines to output file
with open(output_file, "w") as file:
    file.writelines(first_two_lines)

print("First two lines written successfully.")
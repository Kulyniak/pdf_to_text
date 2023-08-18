input_file_path = "parseversion.txt"
output_file_path = "output.txt"

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        modified_line = line.replace(" ", "").replace("\t", "")  # Remove spaces and tabs
        output_file.write(modified_line)

print("Whitespace removed and saved to output.txt")

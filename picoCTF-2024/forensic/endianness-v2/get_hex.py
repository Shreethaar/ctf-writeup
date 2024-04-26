def save_file_hex(input_filename, output_filename):
    with open(input_filename, 'rb') as f:
        file_data = f.read()

    file_hex = file_data.hex()

    with open(output_filename, 'w') as f:
        f.write(file_hex)

input_filename = 'challengefile'  # replace with your input file name
output_filename = 'analyze.txt'  # replace with your output file name
save_file_hex(input_filename, output_filename)
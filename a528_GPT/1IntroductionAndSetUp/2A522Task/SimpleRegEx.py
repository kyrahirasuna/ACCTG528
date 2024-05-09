import re
import csv

# Regular expression pattern
pattern = r'([A-Za-z]{2})(\d+)-(\d+)(\w{2})'

# Open input and output files
with open('1IntroductionAndSetUp/2A522Task/input.csv', 'r') as input_file, open('1IntroductionAndSetUp/2A522Task/output.csv', 'w', newline='') as output_file: 
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    # Write header to output file
    writer.writerow(['Country Code', 'First Number', 'Second Number', 'Measurement Unit'])
    
    # Process each row in the input file
    for row in reader:
        string = row[0]  # Assuming the string is in the first column of the input CSV
        
        # Extracting variables
        match = re.match(pattern, string)
        if match:
            country_code = match.group(1)
            first_number = int(match.group(2))
            second_number = int(match.group(3))
            measurement_unit = match.group(4)
            
            # Write extracted data to output file
            writer.writerow([country_code, first_number, second_number, measurement_unit])
        else:
            print("No match found for:", string)

import csv


# CSV file path
Input_csv_file = "input_file_path?DataInput_withIDs.csv" #made anonymous

# Read data from CSV file
inputData = []
with open(Input_csv_file, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        inputData.append(row)

print("CSV data has been stored in the inputData variable.")

# Write to output data
outputData = [["variants.id","variants.items.id","variants.items.quantity"]]
childSKU_options = ["45289928360249", "45289928393017","45289928425785","45289928458553","45289932390713","45289932423481","45289932456249"] #changed from original values

for i in range(1, len(inputData)):
    lineData = inputData[i]
    variant_ID = lineData[0]
    
    for option in childSKU_options:
        count = lineData.count(option)

        if count > 0:
            newOutputLine = [variant_ID, option, count]
            outputData.append(newOutputLine)

## WRITE TO CSV

# CSV file path
Output_csv_file = "output_file_path/Resultant_file.csv" #made anonymous

# Write data to CSV file
with open(Output_csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(outputData)

print("Data has been written to the CSV file.")

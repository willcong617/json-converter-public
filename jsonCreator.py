import csv
import json

# CSV file path
csv_file = "input_file_path\Resultant_file.csv"

# JSON data structure
json_data = {
    "variants": []
}

# Read data from CSV and populate JSON
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    
    # Skip the header row if present
    header = next(reader, None)
    
    for row in reader:
        variant_id = row[0]
        item_id = row[1]
        quantity = int(row[2])
        
        # Find variant index if it exists
        variant_index = next((index for index, variant in enumerate(json_data["variants"]) if variant["id"] == variant_id), -1)
        
        if variant_index > -1:
            # Variant already exists, append item
            json_data["variants"][variant_index]["items"].append({
                "id": item_id,
                "quantity": quantity
            })
        else:
            # Variant doesn't exist, create new variant
            json_data["variants"].append({
                "id": variant_id,
                "items": [{
                    "id": item_id,
                    "quantity": quantity
                }]
            })

# Convert JSON data to string
json_string = json.dumps(json_data, indent=2)

# Write to JSON file
json_file = "output_file_path\finalData.json"
with open(json_file, mode="w") as file:
    json.dump(json_data, file, indent=2)

# Print the JSON string
print(json_string)

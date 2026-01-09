import csv
import os

input_folder = "data"
output_file = "formatted_sales.csv"

output_rows = []

# Loop through all CSV files in data folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)

        with open(file_path, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Keep only pink morsel (case-insensitive)
                if row["product"].strip().lower() == "pink morsel":
                    
                    # Remove $ sign from price and convert to float
                    price = float(row["price"].replace("$", ""))
                    quantity = int(row["quantity"])

                    sales = price * quantity

                    output_rows.append({
                        "Sales": sales,
                        "Date": row["date"],
                        "Region": row["region"]
                    })

# Write the final combined CSV
with open(output_file, mode="w", newline="") as outfile:
    fieldnames = ["Sales", "Date", "Region"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(output_rows)

print("formatted_sales.csv created successfully with data!")

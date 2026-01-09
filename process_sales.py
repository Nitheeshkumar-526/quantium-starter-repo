import csv
import os

input_folder = "data"
output_file = "formatted_sales.csv"

output_rows = []

for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)

        with open(file_path, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row["product"] == "Pink Morsels":
                    sales = float(row["quantity"]) * float(row["price"])

                    output_rows.append({
                        "Sales": sales,
                        "Date": row["date"],
                        "Region": row["region"]
                    })

with open(output_file, mode="w", newline="") as outfile:
    fieldnames = ["Sales", "Date", "Region"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(output_rows)

print("formatted_sales.csv created successfully!")

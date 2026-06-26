import csv
from pathlib import Path
from re import match
# import case

def read_csv_file(file_path, file_name,Column):
    file_path = Path(file_path)
    filtered_rows = []

    try:
        pattern = f"{file_name}*.csv"
        for csv_file in file_path.glob(pattern):  # goes through all files in the directory that match the pattern
            if csv_file.name.endswith("_filtered.csv"):
                continue

            with csv_file.open("r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) > Column and row[Column].strip() == "Residential": #ex. column is located at index 10 for property type in the csv file
                        filtered_rows.append(row)
        return filtered_rows
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        print(file_path)
        return filtered_rows
    except PermissionError:
        print("Please check the file permissions and try again.")
        return filtered_rows


def print_csv_file(file_path, file_name,Column):
    rows = read_csv_file(file_path, file_name,Column)
    for row in rows:
        print(",".join(row)) #prints all the rows in the filtered list as a single string, with each value separated by a comma
    return rows


def create_csv_file(file_path, file_name,Column):
    rows = read_csv_file(file_path, file_name,Column)
    output_path = file_path / f"{file_name}_filtered.csv"
 
    try:
        with output_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            #make sure all records are on their own rows
        print(f"\nFiltered rows written to {output_path}")
    except PermissionError:
        print("Please check the write permissions and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_path = Path("C:/Users/Viv/Documents/Career readiness/internships/IDX exchange/csv")

    for prefix in ("CRMLSListing", "CRMLSSold"):
        column = -1

        match prefix:
            case "CRMLSListing":
                column = 10  # property type column in the CSV file
            case "CRMLSSold":
                column = 17
            case _:
                print(f"Column for {prefix} is out of range. Please check the column index and try again.")
                continue

        if (column>-1):       
            print_csv_file(file_path, prefix, column)
            create_csv_file(file_path, prefix, column)
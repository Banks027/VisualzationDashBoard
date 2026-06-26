import csv
from pathlib import Path
from re import match
import struct
from types import SimpleNamespace
def MeanCalc(Mean)
    

def MaxCalc(Max)
def MedianCalc(Median)
def PercentilesCalc(Percentiles) 

# Usage
Column= SimpleNamespace(ClosePrice=0, LivingArea=0,DaysOnMarket=0)

ClosePrice= SimpleNamespace(Min=0, Max=0,Mean=0,median=0, percentiles=0)
# Min.x = 15
print(ClosePrice)  # Output: namespace(x=15, y=20)
print(f"ClosePrice Min={ClosePrice.Min}, ClosePrice Max={ClosePrice.Max}, ClosePrice Mean={ClosePrice.Mean},ClosePrice Median={ClosePrice.Median},ClosePrice Percentiles={ClosePrice.Percentiles}")

LivingArea= SimpleNamespace(Min=0, Max=0,Mean=0,median=0, percentiles=0)
DaysOnMarket= SimpleNamespace(Min=0, Max=0,Mean=0,median=0, percentiles=0)


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
                    row and len(row) > Column and row[Column].strip() == "Residential":
                    ClosePrice.Min= 
                    ClosePrice.Max= 
                    ClosePrice.Mean= 
                    
                    #determine unique property types
                    # Null count summary table for columns above 90%
                    #ClosePrice mean, min, max, mean, median, percentiles
                    # LivingArea mean, min, max, mean, median, percentiles
                    # Day on market mean, min, max, mean, median, percentiles
                    #all saved to .csv
   
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
        Column.ClosePrice = -1 #allows for Property type column be located in any column
        Column.LivingArea = -1 
        Column.DaysOnMarket= -1
        match prefix:
            case "CRMLSListing":
                column = 10  # property type column in the CSV file
            case "CRMLSSold":
                column = 17
            case _:
                print(f"Column for {prefix} is out of range. Please check the column index and try again.")
                continue

        if ( Column.DaysOnMarket>-1 |  Column.LivingArea >-1 | Column.ClosePrice >-1):       
            # print_csv_file(file_path, prefix, column)
            read_csv_file(file_path,prefix,Column.ClosePrice)


            create_csv_file(file_path, prefix, column)
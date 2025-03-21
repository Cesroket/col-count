import pandas as pd
import sys
import os

def main(input_file, column_index):
    data = pd.read_csv(input_file, sep='\t')

    if column_index < 1 or column_index > data.shape[1]:
        print(f"Error: The column index '{column_index}' is not correct. The input-file have between 1 & {data.shape[1]} columns.")
        return

    column_data = data.iloc[:, column_index - 1]
    abundance = column_data.value_counts()
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_count-result.txt"

    abundance.to_csv(output_file, header=True, sep='\t')

    print(f"Result save in: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <columna_index>")
    else:
        input_file = sys.argv[1]
        try:
            column_index = int(sys.argv[2])
            main(input_file, column_index)
        except ValueError:
            print(f"Error: The column index is not a number!!")
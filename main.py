import argparse
from input_data import read_dataset
from data_analysis import analyze_column_properties
from output_type import output_data_types
from exploratory_analysis import  exploratory_data_analysis # Make sure this matches your actual import

def main(file_path):
    try:
        df = read_dataset(file_path)
        if df is None or df.empty:
            print("Failed to read the dataset. Please check the file format and ensure it's supported.")
            return 
        data_types = analyze_column_properties(df)
        output_data_types(data_types)

        # Optional: perform exploratory data analysis after outputting data types
        proceed_with_eda = input("Would you like to perform exploratory data analysis on the dataset? (y/n): ")
        if proceed_with_eda.lower() == 'y':
            exploratory_data_analysis(df)

    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        print("Please check the file format and ensure it's supported.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze dataset column types.')
    parser.add_argument('file_path', type=str, help='The path to the dataset file.')
    args = parser.parse_args()
    
    main(args.file_path)

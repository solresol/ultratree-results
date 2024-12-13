import logging
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
import matplotlib.pyplot as plt
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:

    try:
        df = pd.read_csv(file_path)

        # Check and fix duplicate column names
        if df.columns.duplicated().any():
            duplicates = df.columns[df.columns.duplicated()].tolist()
            logging.warning("Duplicate column names found: %s", duplicates)
            df.columns = pd.io.parsers.ParserBase({'names':df.columns})._maybe_dedup_names(df.columns)
        
        if 'model_node_count' not in df.columns:
            logging.warning(
                "'model_node_count' column is missing from the input DataFrame. "
                "The script will proceed without plotting this data. "
                "Please update the CSV file or check the data generation process."
            )
            df['model_node_count'] = None  # Add a placeholder column to allow the script to continue
        return df
    except pd.errors.EmptyDataError:
        logging.error("The CSV file is empty. Please provide a valid CSV file with data.")
        exit(1)
    except pd.errors.ParserError:
        logging.error("Error parsing the CSV file. Please ensure the file is correctly formatted.")
        exit(1)
    except FileNotFoundError:
        logging.error("The specified CSV file was not found. Please check the file path and try again.")
        exit(1)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        exit(1)

def plot_data(df: pd.DataFrame, output_file: str) -> None:
    try:
        grouped = df.groupby('augmentation')
        plt.figure()
        for name, group in grouped:
            plt.plot(group['model_node_count'], group['total_loss'], marker='o', label=name)
        plt.xlabel('Model Node Count')
        plt.title('Total Loss vs Model Node Count')
        plt.ylabel('Total Loss')
        plt.title('Total Loss vs Model Parameter Count')
        plt.legend()
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
    except ValueError as e:
        print(f"Error during plotting: {e}")
        exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(description="Plot total_loss vs model_node_count from a CSV file. The CSV file must contain the columns 'model_node_count' and 'total_loss'.")
    parser.add_argument('--input', default='neural-results.csv', help='Path to the input CSV file.')
    parser.add_argument('--output', default='neural-results.png', help='Path to the output PNG file.')
    args = parser.parse_args()

    df = read_csv(args.input)
    plot_data(df, args.output)

if __name__ == '__main__':
    main()
"""
CSV File Structure
------------------

The input CSV file must contain the following columns:
- `model_node_count`: Integer, represents the count of nodes in the model.
- `total_loss`: Float, represents the total loss value.

Ensure that these columns are present in your CSV file before running the script.
"""

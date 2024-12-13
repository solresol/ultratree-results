import argparse

import matplotlib.pyplot as plt
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        if 'model_node_count' not in df.columns:
            raise ValueError("'model_node_count' column is missing from the input DataFrame. Please ensure the CSV file has the correct structure.")
        return df
    except ValueError as e:
        print(f"Error: {e}")
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
## CSV File Structure

The input CSV file must contain the following columns:
- `model_node_count`: Represents the count of nodes in the model.
- `total_loss`: Represents the total loss value.

Ensure that these columns are present in your CSV file before running the script.

## Verifying CSV Structure

To verify the structure of your CSV file, you can use the following Python snippet with pandas:

```python
import pandas as pd

df = pd.read_csv('your-file.csv')
print(df.columns)
```

This will print the columns present in your CSV file. Make sure `model_node_count` and `total_loss` are listed.

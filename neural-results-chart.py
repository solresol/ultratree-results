import argparse

import matplotlib.pyplot as plt
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    
    return df

def plot_data(df: pd.DataFrame, output_file: str) -> None:
    grouped = df.groupby('augmentation')
    plt.figure()
    for name, group in grouped:
        plt.plot(group['model_parameter_count'], group['total_loss'], marker='o', label=name)
    plt.xlabel('Model Parameter Count')
    plt.ylabel('Total Loss')
    plt.title('Total Loss vs Model Parameter Count')
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

def main() -> None:
    parser = argparse.ArgumentParser(description='Plot total_loss vs model_parameter_count from a CSV file.')
    parser.add_argument('--input', default='neural-results.csv', help='Path to the input CSV file.')
    parser.add_argument('--output', default='neural-results.png', help='Path to the output PNG file.')
    args = parser.parse_args()

    df = read_csv(args.input)
    plot_data(df, args.output)

if __name__ == '__main__':
    main()

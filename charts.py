import argparse
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


def load_data(database: str) -> pd.DataFrame:
    conn = sqlite3.connect(database)
    query = "SELECT * FROM validation_runs"
    df = pd.read_sql_query(query, conn)
    conn.close()
    df['cutoff_date'] = pd.to_datetime(df['cutoff_date'])
    return df

def plot_and_save(df: pd.DataFrame, y_column: str, y_label: str, filename: str) -> None:
    df = df.sort_values(by='cutoff_date')
    plt.figure()
    plt.plot(df['cutoff_date'], df[y_column], marker='o')
    plt.xlabel('Cutoff Date')
    if y_label == 'Total Loss':
        plt.title('Loss on held-out data vs Cutoff Date')
    else:
        plt.title(f'{y_label} vs Cutoff Date')
    plt.ylabel(y_label)
    plt.title(f'{y_label} vs Cutoff Date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def main() -> None:
    parser = argparse.ArgumentParser(description='Generate plots from validation_runs table.')
    parser.add_argument('--database', default='validation.sqlite', help='Path to the SQLite database file.')
    args = parser.parse_args()

    df = load_data(args.database)

    plot_and_save(df, 'total_loss', 'Total Loss', 'total_loss_vs_time.png')
    plot_and_save(df, 'model_node_count', 'Model Node Count', 'model_node_count_vs_time.png')
    plot_and_save(df, 'average_depth', 'Average Depth', 'average_depth_vs_time.png')
    plot_and_save(df, 'average_in_region_hits', 'Average In-Region Hits', 'average_in_region_hits_vs_time.png')

if __name__ == '__main__':
    main()

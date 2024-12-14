import argparse
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


def load_data(database: str) -> pd.DataFrame:
    conn = sqlite3.connect(database)
    query = "SELECT * FROM validation_runs where model_node_count is not null"
    df = pd.read_sql_query(query, conn)
    conn.close()
    df['cutoff_date'] = pd.to_datetime(df['cutoff_date'])
    return df

def plot_and_save(df: pd.DataFrame, x_column: str, x_label: str, y_column: str, y_label: str, filename: str, log_x: bool = False, log_y: bool = False) -> None:
    df = df.sort_values(by=x_column)
    plt.figure()
    #plt.scatter(df[x_column], df[y_column], marker='o')
    plt.plot(df[x_column], df[y_column], marker='o')
    plt.xlabel(x_label)
    if y_label == 'Total Loss':
        plt.title('Loss on held-out data vs {x_label}')
    else:
        plt.title(f'{y_label} vs {x_label}')
    plt.ylabel(y_label)
    plt.title(f'{y_label} vs {x_label}')
    plt.xticks(rotation=45)
    if log_x:
       plt.xscale('log')
    if log_y:
       plt.yscale('log')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()



def main() -> None:
    parser = argparse.ArgumentParser(description='Generate plots from validation_runs table.')
    parser.add_argument('--database', default='validation.sqlite', help='Path to the SQLite database file.')
    args = parser.parse_args()

    df = load_data(args.database)

    plot_and_save(df, 'cutoff_date', 'Model creation date', 'total_loss', 'Loss on held-out data', 'total_loss_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'model_node_count', 'Model Node Count', 'model_node_count_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'average_depth', 'Average Depth', 'average_depth_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'average_in_region_hits', 'Average In-Region Hits', 'average_in_region_hits_vs_time.png')

    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'total_loss_vs_model_size.png', log_y = True)

if __name__ == '__main__':
    main()

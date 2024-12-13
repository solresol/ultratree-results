import argparse
import logging
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

logging.basicConfig(level=logging.INFO)


def load_data(database: str) -> pd.DataFrame:
    conn = sqlite3.connect(database)
    query = "SELECT *, model_node_count FROM validation_runs"
    df = pd.read_sql_query(query, conn)
    conn.close()
    df['cutoff_date'] = pd.to_datetime(df['cutoff_date'])

    duplicated_columns = df.columns.duplicated()
    if duplicated_columns.any():
        logging.info('Duplicate columns detected. Renaming to make them unique.')
        df.columns = pd.io.parsers.ParserBase({'names':df.columns})._maybe_dedup_names(df.columns)
        for i, duplicated in enumerate(duplicated_columns):
            if duplicated:
                new_name = df.columns[i] + '_dup'
                logging.info(f'Renaming \"{df.columns[i]}\" to \"{new_name}\"')
                df = df.rename(columns={df.columns[i]: new_name})

    return df

def plot_and_save(df: pd.DataFrame, x_column: str, x_label: str, y_column: str, y_label: str, filename: str) -> None:
    df = df.sort_values(by=x_column)
    plt.figure()
    plt.plot(df[x_column], df[y_column], marker='o')
    plt.xlabel(x_label)
    if y_label == 'Total Loss':
        plt.title('Loss on held-out data vs {x_label}')
    else:
        plt.title(f'{y_label} vs {x_label}')
    plt.ylabel(y_label)
    plt.title(f'{y_label} vs {x_label}')
    plt.xticks(rotation=45)
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
    logging.info('Starting the plotting process.')
        plot_and_save(df, 'cutoff_date', 'Model creation date', 'average_in_region_hits', 'Average In-Region Hits', 'average_in_region_hits_vs_time.png')

        plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'total_loss_vs_model_size.png')
    except Exception as e:
        logging.error(f'An error occurred during plotting: {e}')
        raise
    finally:
        logging.info('Plotting process completed.')

if __name__ == '__main__':
    main()

import argparse
import sqlite3

import matplotlib.pyplot
import pandas as pd
import os
import sys

def load_data(database: str) -> pd.DataFrame:
    conn = sqlite3.connect(database)
    query = "SELECT * FROM evaluation_runs where model_node_count is not null and total_loss is not null"
    df = pd.read_sql_query(query, conn)
    conn.close()
    df['cutoff_date'] = pd.to_datetime(df['cutoff_date'])
    return df

def plot_and_save(df: pd.DataFrame, x_column: str, x_label: str, y_column: str, y_label: str, filename: str, log_x: bool = False, log_y: bool = False) -> None:
    df = df.sort_values(by=x_column)
    fig, ax = matplotlib.pyplot.subplots()
    for modelfile in sorted(df.model_file.unique()):
        basename = os.path.basename(modelfile)
        if basename == 'tiny.sqlite':
            # Hopefully all references are gone
            basename = 'sense-annotated1.sqlite'
        if not basename.endswith('.sqlite'):
            sys.exit(f"Don't know how to handle the model {modelfile}")
        basename = basename[:-7]
        basename = basename.replace('-', ' ')
        basename = basename[:-1] + ' ' + basename[-1]
        basename = basename.title()
        if ',' in basename:
            basename = 'Ensemble'
        this_model = df[df.model_file == modelfile]
        this_model.set_index(x_column).sort_index()[y_column].plot(label=basename, marker='o')
        #ax.plot(df[x_column], df[y_column], marker='o')
    ax.set_xlabel(x_label)
    if y_label == 'Total Loss':
        ax.set_title('Loss on held-out data vs {x_label}')
    else:
        ax.set_title(f'{y_label} vs {x_label}')
    ax.set_ylabel(y_label)
    ax.set_title(f'{y_label} vs {x_label}')
    ax.legend()
    #ax.set_xticklabels(rotation=45)
    if log_x:
       ax.set_xscale('log')
    if log_y:
       ax.set_yscale('log')
    fig.tight_layout()
    fig.savefig(filename)



def main() -> None:
    parser = argparse.ArgumentParser(description='Generate plots from validation_runs table.')
    parser.add_argument('--database', default='inferences.sqlite', help='Path to the SQLite database file.')
    args = parser.parse_args()

    df = load_data(args.database)

    plot_and_save(df, 'cutoff_date', 'Model creation date', 'total_loss', 'Loss on held-out data', 'total_loss_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'model_node_count', 'Model Node Count', 'model_node_count_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'average_depth', 'Average Depth', 'average_depth_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'average_in_region_hits', 'Average In-Region Hits', 'average_in_region_hits_vs_time.png')

    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'total_loss_vs_model_size.png', log_y = True)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import argparse
import sqlite3
import typing

import matplotlib.pyplot
import pandas as pd
import os
import sys

def load_data(database: str) -> pd.DataFrame:
    conn = sqlite3.connect(database)
    #query = "SELECT * FROM evaluation_runs where model_node_count is not null and total_loss is not null"
    query = """
    select evaluation_run_id, model_file, model_node_count, total_loss, average_depth, average_in_region_hits, cutoff_date, sum(loss) as noun_loss
         from inferences join evaluation_runs using (evaluation_run_id)
        where model_node_count is not null and total_loss is not null
          and correct_path like '1.%.%'
     group by evaluation_run_id, model_file, model_node_count, total_loss, average_depth, average_in_region_hits, cutoff_date
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    df['cutoff_date'] = pd.to_datetime(df['cutoff_date'])
    return df

def modelfile2displayname(modelfile: str) -> str:
    if ',' in modelfile:
        return "Ensemble"
    basename = os.path.basename(modelfile)
    if basename == 'tiny.sqlite':
        sys.exit("Legacy tiny")
        # Hopefully all references are gone
        basename = 'sense-annotated1.sqlite'
    if not basename.endswith('.sqlite'):
        sys.exit(f"Don't know how to handle the model {modelfile}")
    basename = basename[:-7]
    basename = basename.replace('-', ' ')
    if basename[-1].endswith('0'):
        pass
    else:
        basename = basename[:-1] + ' ' + basename[-1]
    basename = basename.title()
    return basename
    

def plot_and_save(df: pd.DataFrame, x_column: str, x_label: str, y_column: str, y_label: str, filename: str, log_x: bool = False, log_y: bool = False, skip_list: list[str] = [], keep_list: list[str] = None, min_x: int = 0) -> None:
    if keep_list and skip_list:
       sys.exit("Had a skip list and a keep list")
    df = df.sort_values(by=x_column)
    if min_x:
        df = df[df[x_column] >= min_x]
    fig, ax = matplotlib.pyplot.subplots()
    display_names = { modelfile2displayname(modelfile) : modelfile for modelfile in df.model_file.unique()}
    if keep_list:
       skip_list = [k for k in display_names.keys() if k not in keep_list]
    for displayname in sorted(display_names.keys()):
        if displayname in skip_list:
            continue
        modelfile = display_names[displayname]
        this_model = df[df.model_file == modelfile]
        marker = 'o'
        linestyle = "-"
        if 'Ensemble' in displayname:
            linestyle = "dashed"
            marker = "^"
        if 'Unannotated' in displayname:
            marker = 'x'
        this_model.set_index(x_column).sort_index()[y_column].plot(label=displayname, marker=marker, linestyle=linestyle)
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
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'noun_loss', 'Loss on nouns in held-out data', 'noun_loss_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'model_node_count', 'Model Node Count', 'model_node_count_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'average_depth', 'Average Depth', 'average_depth_vs_time.png')
    plot_and_save(df, 'cutoff_date', 'Model creation date', 'average_in_region_hits', 'Average In-Region Hits', 'average_in_region_hits_vs_time.png')

    standard_models = [f'Sense Annotated {i}' for i in [1,2,3,4,5]]
    
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'sense_vs_unannotated.png', keep_list = ['Sense Annotated 1', 'Unannotated Model 1'], log_x = False)

    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'levels_of_careful.png', keep_list = ['Sense Annotated 1', 'Careful10', 'Careful100', 'Careful10000'], log_x = True, min_x=2)
    
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'total_loss_vs_model_size.png', skip_list = ['Ensemble'], log_x = True)
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'noun_loss', 'Loss on held-out noun data', 'noun_loss_vs_model_size.png', keep_list = standard_models + ['Ensemble', 'Careful10000'], log_x = True, min_x=2)
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'plain_models_loss_vs_size.png', keep_list = standard_models, log_x = True, min_x=500)
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'exotic_models_loss_vs_size.png', skip_list = standard_models, log_x = True)

    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'careful10000_loss_vs_size.png', keep_list = ['Careful10000'], log_x = True)
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'noun_loss', 'Loss on held-out data', 'careful10000_noun_loss_vs_size.png', keep_list = ['Careful10000'], log_x = True)

    
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'total_loss', 'Loss on held-out data', 'total_loss_vs_model_size_with_ensemble.png', keep_list = ['Sense Annotated 1', 'Ensemble'], log_x=True, min_x=1000)
    plot_and_save(df, 'model_node_count', 'Model Size\n(Node count)', 'noun_loss', 'Loss on held-out noun data', 'noun_loss_vs_model_size_with_ensemble.png', skip_list = ['Unannotated Model 1', 'Careful10', 'Careful100', 'Careful10000'], log_x = True)    

if __name__ == '__main__':
    main()

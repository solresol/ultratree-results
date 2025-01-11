#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import pandas as pd
import sqlite3

def plot_data(df: pd.DataFrame, tree_df: pd.DataFrame, ax: Axes, column_name: str, column_title: str) -> None:
    # just show the #1 model to keep the chart simple
    tree_df = tree_df[tree_df.model_file.str.endswith('1.sqlite') | tree_df.model_file.str.contains(',')]
    for name in sorted(tree_df.model_file.unique()):
        sub_df = tree_df[tree_df.model_file == name]
        if 'unannotated' in name:
            label='Ultra-tree unannotated model'
            continue
        elif ',' in name:
            label="Ensemble"
        else:
            label='Ultra-tree sense annotated model'
            continue
        sub_df.set_index('model_node_count').sort_index()[column_name].plot(ax=ax, label=label, marker="^", color="red", linestyle="dashed")
    for name in sorted(df.augmentation.unique()):
        df[df.augmentation == name].set_index('model_parameter_count')[column_name].plot(ax=ax, marker='o', label=f"{name} neural")
    ax.set_xlabel('Model Parameter Count')
    ax.set_ylabel(f'{column_title}')
    ax.set_title(f'{column_title} vs Model Parameter Count')
    ax.set_xscale('log')
    #ax.set_yscale('log')
    ax.legend()

def main() -> None:
    parser = argparse.ArgumentParser(description='Plot total_loss vs model_parameter_count from a CSV file.')
    parser.add_argument('--input', default='neural-results.csv', help='Path to the input CSV file.')
    parser.add_argument('--output', default='neural-results.png', help='Path to the output PNG file.')
    parser.add_argument("--noun-output", default="noun-baseline.png", help="Path to the output PNG file for losses on nouns")
    parser.add_argument('--tree-data-input', default='inferences.sqlite', help="SQLite database with inference results")
    args = parser.parse_args()

    neural_df = pd.read_csv(args.input).sort_values('model_parameter_count')
    conn = sqlite3.connect(args.tree_data_input)
    tree_df = pd.read_sql("""
       select evaluation_run_id, model_file, model_node_count, total_loss, sum(loss) as noun_loss
         from inferences join evaluation_runs using (evaluation_run_id)
        where model_node_count is not null and total_loss is not null
          and correct_path like '1.%.%'
     group by evaluation_run_id, model_file, model_node_count, total_loss
      """, conn)

    fig, ax = plt.subplots()
    plot_data(neural_df, tree_df, ax, 'total_loss', "Total Loss")
    fig.tight_layout()
    fig.savefig(args.output)

    fig, ax = plt.subplots()    
    plot_data(neural_df, tree_df, ax, 'noun_loss', "Noun Loss")
    fig.tight_layout()
    fig.savefig(args.noun_output)    

if __name__ == '__main__':
    main()

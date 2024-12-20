import argparse

import matplotlib.pyplot
import pandas as pd
import sqlite3

def plot_data(df: pd.DataFrame, tree_df: pd.DataFrame, output_file: str) -> None:
    fig, ax = matplotlib.pyplot.subplots()
    # just show the #1 model to keep the chart simple
    tree_df = tree_df[tree_df.model_file.str.endswith('1.sqlite') | tree_df.model_file.str.contains(',')]
    for name in sorted(tree_df.model_file.unique()):
        sub_df = tree_df[tree_df.model_file == name]
        if 'unannotated' in name:
            label='Ultra-tree unannotated model'
        elif ',' in name:
            label="Ensemble"
        else:
            label='Ultra-tree sense annotated model'
        sub_df.set_index('model_node_count').sort_index().total_loss.plot(ax=ax, label=label, marker="o")
    for name in sorted(df.augmentation.unique()):
        df[df.augmentation == name].set_index('model_parameter_count').total_loss.plot(ax=ax, marker='o', label=f"{name} neural")
    ax.set_xlabel('Model Parameter Count')
    ax.set_ylabel('Total Loss')
    ax.set_title('Total Loss vs Model Parameter Count')
    ax.set_xscale('log')
    #ax.set_yscale('log')
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_file)

def main() -> None:
    parser = argparse.ArgumentParser(description='Plot total_loss vs model_parameter_count from a CSV file.')
    parser.add_argument('--input', default='neural-results.csv', help='Path to the input CSV file.')
    parser.add_argument('--output', default='neural-results.png', help='Path to the output PNG file.')
    parser.add_argument('--tree-data-input', default='inferences.sqlite', help="SQLite database with inference results")
    args = parser.parse_args()

    neural_df = pd.read_csv(args.input).sort_values('model_parameter_count')
    conn = sqlite3.connect(args.tree_data_input)
    tree_df = pd.read_sql('select * from evaluation_runs where model_node_count is not null and total_loss is not null', conn)
    
    plot_data(neural_df, tree_df, args.output)

if __name__ == '__main__':
    main()

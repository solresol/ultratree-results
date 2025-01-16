#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import pandas as pd
import sqlite3
import math
import sklearn.linear_model

def extrapolate(series):
    starting_point = math.log10(series.index.max())
    ending_point = 7 ; # 10,000,000 nodes -- the size of the largest neural model
    extrapolation_x = [starting_point]
    extrapolation_x += range(int(starting_point)+1,ending_point+1)
    extrapolation_dataframe = pd.DataFrame({'log_parameter_count': extrapolation_x})
    training_data = pd.DataFrame({'loss': series})
    training_data['parameter_count'] = training_data.index
    training_data['log_parameter_count'] = training_data.parameter_count.map(math.log10)
    ts = sklearn.linear_model.TheilSenRegressor()
    ts.fit(training_data[['log_parameter_count']], training_data.loss)
    extrapolation_dataframe['loss'] = ts.predict(extrapolation_dataframe[['log_parameter_count']])
    extrapolation_dataframe['parameter_count'] = extrapolation_dataframe.log_parameter_count.map(lambda x: 10 ** x)
    #print(ts.coef_)
    return extrapolation_dataframe

def plot_data(df: pd.DataFrame, tree_df: pd.DataFrame, ax: Axes, column_name: str, column_title: str, do_extrapolate: bool = True) -> None:
    # just show the #1 model to keep the chart simple
    tree_df = tree_df[tree_df.model_file.str.endswith('1.sqlite') | tree_df.model_file.str.contains(',') | tree_df.model_file.str.contains('careful10000')]
    for name in sorted(tree_df.model_file.unique()):
        sub_df = tree_df[tree_df.model_file == name]
        if 'unannotated' in name:
            label='Ultra-tree unannotated model'
            continue
        elif ',' in name:
            label="Ensemble"
            marker = '^'
            color = "orange"
        elif 'careful10000' in name:
            label="Careful 10000"
            marker = "+"
            color = "purple"
        else:
            label='Ultra-tree sense annotated model'
            continue
        sub_df.set_index('model_node_count').sort_index()[column_name].plot(ax=ax, label=label, marker=marker, color=color)
        #print(label)
        if do_extrapolate:
            extrapolation = extrapolate(sub_df.set_index('model_node_count')[column_name])
            extrapolation.set_index('parameter_count').loss.plot(ax=ax, label=f"Extrapolation of {label}",
                                                                 linestyle="dotted",
                                                                     marker="", color=color)
            #print(extrapolation)
                                    
    for name in sorted(df.augmentation.unique()):
        df[df.augmentation == name].set_index('model_parameter_count')[column_name].plot(ax=ax, marker='o', label=f"{name} neural")
    ax.set_xlabel('Model Parameter Count')
    ax.set_ylabel(f'{column_title}')
    ax.set_title(f'{column_title} vs Model Parameter Count')
    ax.set_xscale('log')
    #ax.set_yscale('log')
    ax.legend()

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Plot total_loss vs model_parameter_count from a CSV file.')
    parser.add_argument('--input', default='neural-results.csv', help='Path to the input CSV file.')
    parser.add_argument('--output', default='neural-results.png', help='Path to the output PNG file.')
    parser.add_argument("--noun-output", default="noun-baseline.png", help="Path to the output PNG file for losses on nouns")
    parser.add_argument('--tree-data-input', default='inferences.sqlite', help="SQLite database with inference results")
    args: argparse.Namespace = parser.parse_args()

    neural_df: pd.DataFrame = pd.read_csv(args.input).sort_values('model_parameter_count')
    conn: sqlite3.Connection = sqlite3.connect(args.tree_data_input)
    tree_df: pd.DataFrame = pd.read_sql("""
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
    plot_data(neural_df, tree_df, ax, 'noun_loss', "Noun Loss", do_extrapolate=False)
    fig.tight_layout()
    fig.savefig(args.noun_output)    
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
    plot_data(neural_df, tree_df, ax, 'noun_loss', "Noun Loss", do_extrapolate=False)
    fig.tight_layout()
    fig.savefig(args.noun_output)    

if __name__ == '__main__':
    main()

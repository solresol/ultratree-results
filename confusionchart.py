#!/usr/bin/env python3

import argparse
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Part of speech mapping
POS_MAPPING = {
    '1': 'noun',
    '2': 'adjective',
    '3': 'verb',
    '4': 'adverb',
    '5': 'punctuation',
    '6': 'preposition',
    '7': 'articles',
    '8': 'other'
}

def get_first_element(path):
    """Extract first element from dot-separated path"""
    return path.split('.')[0] if path else ''

def map_pos(pos_num):
    """Map numeric POS to string label"""
    return POS_MAPPING.get(pos_num, 'unknown')

def load_and_process_data(conn, run_id, key_name):
    # Query data
    query = f"""
    SELECT predicted_path, correct_path
    FROM inferences
    WHERE {key_name}_run_id = ?
    """
    
    # Load into dataframe
    df = pd.read_sql_query(query, conn, params=(run_id,))
    
    # Extract first element from paths and map to POS labels
    df['predicted_part_of_speech'] = df['predicted_path'].apply(get_first_element).apply(map_pos)
    df['correct_part_of_speech'] = df['correct_path'].apply(get_first_element).apply(map_pos)
    
    return df

def create_confusion_matrix(df: pd.DataFrame) -> plt.Figure:
    """Create confusion matrix and plot heatmap"""
    # Create confusion matrix
    confusion = pd.crosstab(
        df['correct_part_of_speech'],
        df['predicted_part_of_speech'],
        #normalize='index'  # Normalize by rows
    )
    
    # Create heatmap
    plt.figure(figsize=(12, 4))
    sns.heatmap(
        confusion,
        annot=True,  # Show numbers in cells
        fmt='.2f',   # Format as percentage
        cmap='YlOrRd',
        #square=True,
        #cbar_kws={'label': 'Proportion'}
    )
    
    plt.title('Part of Speech Prediction Confusion Matrix')
    plt.ylabel('True Part of Speech')
    plt.xlabel('Predicted Part of Speech')
    
    return plt.gcf()

def main() -> None:
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate POS confusion matrix from inference data')
    parser.add_argument('--dbpath', help='Path to SQLite database', required=True)
    parser.add_argument('--run-id', type=int, help='Validation run ID to analyze', required=True)
    parser.add_argument('--output-path', help='Path to save the confusion matrix plot', required=True)
    parser.add_argument("--key-name", choices=['validation', 'evaluation'], default='validation')
    # Parse arguments
    args = parser.parse_args()

    conn = sqlite3.connect(args.dbpath)
    
    # Load and process data
    df = load_and_process_data(conn, args.run_id, args.key_name)
    
    # Create and save plot
    fig = create_confusion_matrix(df)
    fig.savefig(args.output_path, bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"Confusion matrix saved to {args.output_path}")
    conn.close()    

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import argparse
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import os

def fetch_histogram_data(db_path, target_filename):
    """
    Fetch the most recent histogram data for the given filename.
    
    Args:
        db_path (str): Path to the SQLite database
        target_filename (str): Original filename to look up
        
    Returns:
        tuple: (snapshot_id, timestamp, DataFrame with k and appearance_count)
    """
    conn = sqlite3.connect(db_path)
    
    # First get the most recent snapshot for this filename
    snapshot_query = """
    SELECT context_snapshot_id, when_captured
    FROM context_snapshots
    WHERE filename = ?
    ORDER BY when_captured DESC
    LIMIT 1
    """
    
    cursor = conn.execute(snapshot_query, (target_filename,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        raise ValueError(f"No snapshots found for filename: {target_filename}")
        
    snapshot_id, timestamp = row
    
    # Now get the histogram data for this snapshot
    histogram_query = """
    SELECT k, appearance_count
    FROM context_usage
    WHERE context_snapshot_id = ?
    ORDER BY k
    """
    
    df = pd.read_sql_query(histogram_query, conn, params=(snapshot_id,))
    conn.close()
    
    return snapshot_id, timestamp, df

def create_bar_chart(df, output_path, title=None, timestamp=None, model_filename=None):
    """
    Create a bar chart from the histogram data.
    
    Args:
        df (pandas.DataFrame): DataFrame with k and appearance_count columns
        output_path (str): Path where to save the image
        title (str, optional): Custom title for the chart
        timestamp (str, optional): When the snapshot was captured
    """
    plt.figure(figsize=(12, 6))
    
    # Create the bar chart
    plt.bar(df['k'], df['appearance_count'], color='skyblue', edgecolor='black')
    
    # Customize the chart
    plt.xlabel('Context (1 = predecessor word)')
    plt.ylabel('Number of nodes using this context')
    
    # Generate title
    if title:
        chart_title = title
    else:
        chart_title = 'Distribution of Context Usage'
    
    # Add timestamp information in smaller text below main title
    if timestamp:
        chart_title += f'\nSnapshot from {timestamp}'
    if model_filename:
        model_filename = os.path.basename(model_filename)
        if model_filename.endswith('.sqlite'):
            model_filename = model_filename[:-7]
        chart_title += f'\nModel: {model_filename}'
    
    plt.title(chart_title)
    
    # Add grid for better readability
    plt.grid(True, axis='y', alpha=0.3)
    
    # Rotate x-axis labels if there are many values
    if len(df) > 10:
        plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create a bar chart from histogram data in SQLite database'
    )
    
    parser.add_argument(
        '--database',
        help='Path to the SQLite database containing histogram data'
    )
    parser.add_argument(
        '--output',
        help='Path where to save the bar chart image'
    )
    parser.add_argument(
        '--filename',
        help='Original filename to look up in the database'
    )
    parser.add_argument(
        '--title',
        '-t',
        help='Custom title for the bar chart',
        default=None
    )
    
    args = parser.parse_args()
    # Fetch the data
    snapshot_id, timestamp, df = fetch_histogram_data(
        args.database,
        args.filename
    )
        
    # Create the visualization
    create_bar_chart(
        df,
        args.output,
        args.title,
        timestamp,
        args.filename
    )
    
    print(f"Bar chart successfully saved to {args.output}")
    print(f"Used snapshot {snapshot_id} from {timestamp}")


#!/usr/bin/env python3

import sqlite3
import argparse
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_time_gaps(database_path, cutoff_threshold):
    """
    Fetch time gaps between successive timestamps from the SQLite database,
    filtering out gaps larger than the cutoff threshold and zero-second gaps.
    """
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Query to fetch successive timestamps and compute time gaps
    cursor.execute(
        """
        WITH OrderedNodes AS (
            SELECT 
                id,
                when_created,
                LAG(when_created) OVER (ORDER BY when_created) AS previous_created
            FROM nodes
        )
        SELECT 
            when_created, 
            previous_created,
            (JULIANDAY(when_created) - JULIANDAY(previous_created)) * 24 * 60 * 60 AS gap_seconds
        FROM OrderedNodes
        WHERE previous_created IS NOT NULL;
        """
    )

    gaps = []
    for row in cursor.fetchall():
        gap_seconds = row[2]
        if gap_seconds > 0 and gap_seconds <= cutoff_threshold:
            gaps.append(gap_seconds)

    connection.close()
    return gaps

def plot_histogram(gaps, cutoff_threshold, output_path):
    """Plot a histogram of the time gaps."""
    fig, ax = plt.subplots()
    ax.hist(gaps, bins=50, edgecolor='black')
    ax.set_title(f'Histogram of Node Creation Time Gaps (Cutoff: {cutoff_threshold} seconds)')
    ax.set_xlabel('Time Gap (seconds)')
    ax.set_ylabel('Frequency')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    fig.savefig(output_path)

def main():
    parser = argparse.ArgumentParser(description="Plot a histogram of time gaps between node creation timestamps.")
    parser.add_argument('--database', type=str, help="Path to the SQLite database.", required=True)
    parser.add_argument('--cutoff', type=int, default=86400, help="Upper cutoff threshold for time gaps in seconds.")
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    # Fetch time gaps from the database
    gaps = fetch_time_gaps(args.database, args.cutoff)

    if gaps:
        print(f"Fetched {len(gaps)} time gaps under the cutoff threshold.")
        # Plot the histogram
        plot_histogram(gaps, args.cutoff, args.output)
    else:
        print("No valid time gaps found under the given cutoff threshold.")

if __name__ == '__main__':
    main()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from typing import Callable

# --- 1. INPUT DATA FILE ---
# Start date (YYYYMMDD) followed by daily stock price data
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data2.csv')

COL_NAMES = ['Stock_Price']
# Set a daily frequency for better slicing examples
FREQ = 'D'

# --- 2. HINT IMPLEMENTATIONS ---
# Define a lambda function to convert strings to Pandas date format:
date_converter: Callable[[str], pd.Timestamp] = lambda x: pd.to_datetime(x, format='%Y%m%d')

# Define a function to read the data from the input file:
def read_data(filepath: str) -> pd.DataFrame:
    # Read CSV file, skipping the first row (date)
    return pd.read_csv(filepath, header=None, skiprows=1)

# Use lambda to get the start date from the first line:
def get_start_date(filepath: str) -> pd.Timestamp:
    with open(filepath, 'r') as f:
        return date_converter(f.readline().strip())

def create_date_index(start_date: pd.Timestamp, num_entries: int) -> pd.DatetimeIndex:
    # Create a list of indices with dates using the start date and frequency:
    return pd.date_range(start=start_date, periods=num_entries, freq=FREQ)

# Create pandas data series using the timestamps:
def create_time_series(data_df: pd.DataFrame, date_index: pd.DatetimeIndex) -> pd.Series:
    return pd.Series(data_df.iloc[:, 0].values, index=date_index, name=COL_NAMES[0])

# --- 3. MAIN LOGIC (SLICING & VISUALIZATION) ---
def main():
    # Define the main function and specify the input file:
    data_df = read_data(DATA_FILE)
    start_date = get_start_date(DATA_FILE)
    
    num_entries = len(data_df)
    date_index = create_date_index(start_date, num_entries)
    
    # Create the full time-series
    ts = create_time_series(data_df, date_index)

    # Define slicing intervals using timestamps
    slices = {
        "Full Range (Daily)": ('2024-01-01', '2024-01-12'),
        "First Week": ('2024-01-01', '2024-01-07'),
        "Specific Interval": ('2024-01-05', '2024-01-09')
    }
    
    plt.figure(figsize=(12, 8))
    
    # Iterate through intervals, slice by timestamp, and plot
    for i, (title, interval) in enumerate(slices.items()):
        
        # SLICING using timestamps
        start, end = interval
        sliced_ts = ts[start:end]
        
        # Plotting the sliced data
        plt.subplot(3, 1, i + 1)
        sliced_ts.plot()
        plt.title(f"{title}: Data Sliced from {start} to {end}", fontsize=10)
        plt.ylabel(ts.name)
        plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
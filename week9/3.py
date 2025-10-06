import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# --- 1. INPUT DATA FILE (Multiple Years for Slicing) ---
# Start date is 20240101. Data columns are: Col 1, Col 2, Col 3, Col 4
# We will use 24 monthly entries for better examples.
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data3.csv')

# Define the function to read the data from the input file (reused from 'timeseries')
def read_data(filepath):
    with open(filepath, 'r') as f:
        start_date = pd.to_datetime(f.readline().strip(), format='%Y%m%d')
    data_df = pd.read_csv(filepath, header=None, skiprows=1)
    
    num_entries = len(data_df)
    date_index = pd.date_range(start=start_date, periods=num_entries, freq='MS')
    
    # Return DataFrame with DatetimeIndex
    return pd.DataFrame(data_df.values, index=date_index)

def main():
    # Define the input filename and load data
    data_df = read_data(DATA_FILE)
    
    # Load the third (index 2) and fourth (index 3) columns into separate variables.
    col_c = data_df.iloc[:, 2]  # Index 2 is the 3rd column
    col_d = data_df.iloc[:, 3]  # Index 3 is the 4th column
    
    # Create a Pandas dataframe object by naming the two dimensions
    ts_df = pd.DataFrame({'Series_C': col_c, 'Series_D': col_d})

    # Perform operation: Create a new series which is the sum of C and D
    ts_df['Series_Sum'] = ts_df['Series_C'] + ts_df['Series_D']

    print("--- 1. FULL DATASET SUMMARY ---")
    print(ts_df.head())
    print("-" * 40)
    
    # Plot the data by specifying the start and end years (Time-based slicing)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Plotting for specific time period (2024)
    ts_df.loc['2024'].plot(ax=ax1)
    ax1.set_title('Time-Series Data: All Series in 2024')
    ax1.set_ylabel('Value')
    ax1.grid(True)

    # --- Filtering the data using conditions and then displaying it ---
    
    # Condition: Series C must be greater than 40
    condition = ts_df['Series_C'] > 40
    filtered_df = ts_df[condition]
    
    # Display the filtered data
    print("--- 2. FILTERED DATA (Series_C > 40) ---")
    print(filtered_df)
    
    # Display the summarized results also
    print("\n--- 3. SUMMARIZED RESULTS (Filtered Data) ---")
    print(filtered_df.describe())

    # Plotting the filtered data points (only where condition is true)
    ts_df['Series_Sum'].plot(ax=ax2, label='Original Sum', alpha=0.5, linestyle='--')
    filtered_df['Series_Sum'].plot(ax=ax2, style='o', label='Filtered Points (C > 40)', color='red')
    ax2.set_title('Filtered Data: Series Sum (Points where Series C > 40)')
    ax2.set_ylabel('Value')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the input file path
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data1.csv')

# Define a function to read the data from the input file
def read_data(filepath):
    # Read CSV file, skipping the first row (date)
    return pd.read_csv(filepath, header=None, skiprows=1)

# Define a lambda function to convert strings to Pandas date format:
date_converter = lambda x: pd.to_datetime(x, format='%Y%m%d')

def main():
    # Specify the columns that contain the data:
    COL_NAMES = ['Stock_Price', 'Oil_Futures', 'Housing_Index']
    
    # Read the start date from the first line of the file
    with open(DATA_FILE, 'r') as f:
        start_date = date_converter(f.readline().strip())
    
    # Read the data rows
    data_df = read_data(DATA_FILE)
    num_entries = len(data_df)
    
    # Create list of indices with dates using start/end with monthly frequency:
    date_index = pd.date_range(start=start_date, periods=num_entries, freq='MS')
    
    # Iterate through the columns, create data series, and plot
    plt.figure(figsize=(10, 6))
    print("Time-Series Data Dimensions:")
    
    for i, col_name in enumerate(COL_NAMES):
        # Create pandas data series using the timestamps:
        ts = pd.Series(data_df.iloc[:, i].values, index=date_index, name=col_name)
        
        # Print dimension details
        print(f"  {ts.name}: Shape={ts.shape}, Index Type={type(ts.index).__name__}")

        # Plot the time-series data
        plt.plot(ts, label=ts.name)

    plt.title('Time-Series Data')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

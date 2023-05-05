import numpy as np
import pandas as pd


def csv_to_np_array(csv_path, fill_value=np.nan):
    try:
        # Load CSV file
        df = pd.read_csv(csv_path, dtype=str)

        # Check if CSV file is empty
        if df.empty:
            raise ValueError('CSV file is empty.')

        # Check if there are any missing values
        if df.isnull().values.any():
            print(f'Warning: CSV file contains missing values. Missing values will be filled with the default numpy filler: {fill_value}.')

        # Fill missing values with default numpy filler
        df.fillna(fill_value, inplace=True)

        # Convert CSV data to numpy array
        data = df.to_numpy()

        return data
    except FileNotFoundError:
        print('CSV file not found.')
        return None
    except ValueError as e:
        print(f'Conversion failed. {e}')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

import numpy as np
import pandas as pd


def csv_to_npz(csv_path, npz_path, fill_value=np.nan):
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

        # Save header and data as separate arrays
        header = df.columns.values
        data = df.to_numpy()

        # Save numpy arrays to NPZ file
        np.savez(npz_path, header=header, data=data)

        print('Conversion successful.')
    except FileNotFoundError:
        print('CSV file not found.')
    except ValueError as e:
        print(f'Conversion failed. {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

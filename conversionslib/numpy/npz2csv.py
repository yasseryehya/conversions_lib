import numpy as np
import pandas as pd


def npz_to_csv(npz_path, csv_path):
    try:
        # Load NPZ file
        data = np.load(npz_path, allow_pickle=True)

        # Get header and data from NPZ file
        header = data['header']
        data = data['data']

        # Convert NPZ data to pandas dataframe
        df = pd.DataFrame(data, columns=header)

        # Save dataframe to CSV file
        df.to_csv(csv_path, index=False)

        print('Conversion successful.')
    except FileNotFoundError:
        print('NPZ file not found.')
    except ValueError as e:
        print(f'Conversion failed. {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

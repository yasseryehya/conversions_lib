import numpy as np
import pandas as pd


def npz_to_np_array(npz_path):
    try:
        # Load NPZ file
        data = np.load(npz_path, allow_pickle=True)

        # Get data from NPZ file
        data = data['data']

        return data
    except FileNotFoundError:
        print('NPZ file not found.')
        return None
    except ValueError as e:
        print(f'Conversion failed. {e}')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

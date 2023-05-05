# csv2npz

`csv2npz` is a Python library that provides a simple function to convert CSV files to NumPy's compressed binary format (`.npz`).

## Installation

You can install `csv2npz` using pip:
```bash
pip install csv2npz
```

## Usage

Here's an example of how to use `csv2npz`:

```python
import csv2npz

csv_file_path = 'my_data.csv'
npz_file_path = 'my_data.npz'

csv2npz.convert(csv_file_path, npz_file_path)
```

`csv2npz.convert` function takes two arguments: the path to the CSV file and the path to the resulting NPZ file. If the CSV file contains a header row, it will be ignored by the function.

## Contributing

Contributions are welcome! If you have any bug reports, feature requests, or patches, please submit them on the [GitHub page](TODO).

## License
This project is licensed under the terms of the MIT license.
""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
from sklearn.preprocessing import StandardScaler

def main(infile, outfile):
    # Load data from CSV file
    data = pd.read_csv(infile)

    # Create StandardScaler object
    scaler = StandardScaler()

    # Apply standard scaling to data
    scaled_data = scaler.fit_transform(data)

    # Write scaled data to CSV file
    pd.DataFrame(scaled_data).to_csv(outfile, index=False)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    parser = argparse.ArgumentParser(
        description='This program applies a standard scale transform to the data in infile and writes it to outfile.')

    # Add positional arguments for input and output filenames
    parser.add_argument('infile', type=str, help='Input filename for the data file that needs to be processed.')
    parser.add_argument('outfile', type=str, help='Output filename.')

    # Parse command-line arguments
    args = parser.parse_args()

    # Call main function with input and output filenames
    main(args.infile, args.outfile)

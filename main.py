# Load libraries
import argparse
from script import run_model

parser = argparse.ArgumentParser()
parser.add_argument("--inputs", nargs='*', help="Input file", required=True)
parser.add_argument("--variables", nargs='*', help="Variables to be used", required=True)
parser.add_argument("--summary", help="Summary", default=None)
parser.add_argument("--r_squared", help="p value", default=None)
args = parser.parse_args()

def parsed_args(args):
    inputs = args.inputs
    variables = args.variables
    summary = args.summary
    r_squared = args.r_squared
    return inputs, variables, summary, r_squared

def main():
    inputs, variables, summary, r_squared = parsed_args(args)
    run_model(inputs, variables, summary, r_squared)

if __name__ == "__main__":
    main()
    exit(0)
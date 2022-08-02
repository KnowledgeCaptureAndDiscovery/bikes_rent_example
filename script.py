# Load libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inputs", nargs='*', help="Input file", required=True)
parser.add_argument("--variables", nargs='*', help="Variables to be used", required=True)
parser.add_argument("--summary", help="Summary", default="summary.txt")
parser.add_argument("--p_value", help="p value", default="p_value")
args = parser.parse_args()

def merge_multiple_dataframe(inputs):
    df = pd.DataFrame()
    for input in inputs:
        df = df.append(pd.read_csv(input))
    return df

def map_variable_name(variable: str) -> str:
    """Find the csv variable name from a full name
    For example: temperature -> temp

    Args:
        variable (str): full name 

    Returns:
        str: csv variable name
    """
    map_dict = {
        "temperature": "temp",
        "humidity": "hum",
        "wind": "windspeed"
    }
    if variable in map_dict:
        return map_dict[variable]
    return None

def check_variables(variables, df):
    for index in range(len(variables)):
        variable = variables[index]
        if variable not in df.columns:
            if map_variable_name(variable) is None:
                print("Variable " + variable + " not found in dataframe")
                exit(1)
            variables[index] = map_variable_name(variable)



# Import data
bikes = merge_multiple_dataframe(args.inputs)

# Get headers of the dataframe
arg_variables = args.variables

# Convert to lowercase array
arg_variables = [variable.lower() for variable in arg_variables]

check_variables(arg_variables, bikes)
# concatenate list of strings using comma
model_variables = " + ".join(arg_variables)
model_variables = "cnt" + " ~ " + model_variables
print(f"""Using variables: {model_variables}""")

# Fit model1
model1 = sm.OLS.from_formula(model_variables, data=bikes).fit()

with open(args.summary, "w") as f:
    f.write(str(model1.summary()))
with open(args.p_value, "w") as f:
    f.write(str(model1.pvalues[0]))

print(model1.summary())

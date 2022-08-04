# Load libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm


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
        "wind": "windspeed",
        "wind speed": "windspeed",
        "month": "mnth",
        "workday": "workingday",
        "weather situation": "weathersit",
        "ambient temperature": "atemp",

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

def parsed_args(args):
    inputs = args.inputs
    variables = args.variables
    summary = args.summary
    r_squared = args.r_squared
    return inputs, variables, summary, r_squared


def write_file(file, content):
    with open(file, "w") as f:
        f.write(content)

def run_model(inputs, variables, summary_output, r_squared_output):
    """
    Args:
        inputs (list): list of input files
        variables (list): list of variables to be used
        summary_output (str): output file for summary
        r_squared_output (str): output file for r_squared

    Returns:
        None
    """
    data = merge_multiple_dataframe(inputs)
    # Convert to lowercase array
    if not isinstance(variables, list):
        variables = list(variables)
    if "None" in variables:
        variables.remove("None")
    variables = [variable.lower() for variable in variables]
    check_variables(variables, data)
    # concatenate list of strings using comma
    model_variables = " + ".join(variables)
    model_variables = "cnt" + " ~ " + model_variables
    print(f"""Using variables: {model_variables}""")

    model = sm.OLS.from_formula(model_variables, data=data).fit()

    if r_squared_output is not None:
        write_file(r_squared_output, str(model.rsquared))
    else:
        print(f"""R squared: {model.rsquared}""")
    
    if summary_output is not None:
        write_file(summary_output, model.summary().as_text())
    else:
        print(model.summary().as_text())

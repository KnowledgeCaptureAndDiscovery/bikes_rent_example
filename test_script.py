from cProfile import run
from itertools import combinations, permutations
from script import run_model

def test_file1_method1():
    variables = ["Temperature", "Ambient Temperature", "Humidity", "Wind Speed", "Season", "Month", "Holiday", "Weekday", "Workday", "Weather Situation", "None"]
    perm = combinations(variables, 6) 
    for p in perm:
        run_model(["data/bikes-2019-2020-ny.csv"], p, None, None)

def test_file1_method2():
    variables = ["Temperature", "Ambient Temperature", "None", "None", "Season", "Month", "Holiday", "Weekday", "Workday", "Weather Situation", "None"]
    run_model(["data/bikes-2019-2020-ny.csv"], variables, None, None)


def test_file1_method3():
    variables = ["Temperature", "Temperature", "None", "None", "Season", "Month", "Holiday", "Weekday", "Workday", "Weather Situation", "None"]
    run_model(["data/bikes-2019-2020-ny.csv"], variables, None, None)
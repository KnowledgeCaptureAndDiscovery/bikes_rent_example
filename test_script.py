from cProfile import run
from itertools import combinations, permutations
from script import run_model

variables = ["Temperature", "Ambient Temperature", "Humidity", "Wind Speed", "Season", "Month", "Holiday", "Weekday", "Workday", "Weather Situation"]
perm = combinations(variables, 6) 
for p in perm:
    run_model(["data/bikes-2019-2020-ny.csv"], p, "test.txt", None)

# AoC 2019 Day 1

# Load packages
import pandas as pd
import numpy as np

# Load input
inputValues = pd.read_table("aoc2019_day1_input.txt",
                            header=None,
                            names=["mass"])

# Part 1
# Calculate fuel by dividing by 3, rounding down and subtracting 2

inputValues["fuel"] = (inputValues["mass"]//3) - 2
totalFuel = inputValues.fuel.sum()

# Part 2
# Calculate fuel need for fuel via the same formula
# Negative fuel counts as needing 0 fuel

# Create a column of zeros to compare to
inputValues["min_fuel"] = 0

# Initialise counters
thisFuel = totalFuel.copy()
newTotalFuel = totalFuel.copy()

# Iteratively update fuel to be the latest fuel need
# Track current value for while loop control and running total for solution
while thisFuel > 0:
    inputValues["fuel"] = (inputValues["fuel"]//3) - 2
    inputValues["fuel"] = np.maximum(inputValues["fuel"], inputValues["min_fuel"])
    thisFuel = inputValues.fuel.sum()
    newTotalFuel += thisFuel

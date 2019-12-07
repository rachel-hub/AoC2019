# AoC 2019 Day 6

# Packages

import pandas as pd
import numpy as np

# Inputs

# InputData = np.loadtxt("aoc2019_day6_input.txt",
#                        dtype='str',
#                        delimiter=",")

# InputData = pd.read_table("aoc2019_day6_input.txt",
#                           sep = ",")

InputData = np.loadtxt("aoc2019_day6_input.txt",
                       dtype='str')

InputData = pd.DataFrame(InputData,
                         columns = ["Input"])

splitInput = InputData["Input"].str.split(")", expand = True)

InputData["Centre"] = splitInput[0]
InputData["Orbiter"] = splitInput[1]

DistinctPlanets = pd.concat([splitInput[0], splitInput[1]]).unique()
DistinctPlanets = pd.DataFrame(DistinctPlanets,
                               columns = ["Planets"])
SquareInputData = InputData.pivot(index="Centre", columns="Orbiter")

DistinctPlanets["dummy"] = 1
AllPlanets = DistinctPlanets.merge(DistinctPlanets, on="dummy", how="outer")
AllPlanets = AllPlanets.rename(columns={"Planets_x":"Centre", "Planets_y": "Orbiter"})
AllPlanets = AllPlanets.merge(InputData, on = ["Centre", "Orbiter"], how="left")
AllPlanets.loc[pd.notnull(AllPlanets["Input"]), "InOrbit"] = 1
AllPlanets.loc[pd.isnull(AllPlanets["Input"]), "InOrbit"] = 0
AllPlanets = AllPlanets[["Centre", "Orbiter", "InOrbit"]]


AllPlanetsPivot = AllPlanets.pivot(index="Centre", columns="Orbiter", values="InOrbit")
AdjacencyMatrix = np.array(AllPlanetsPivot)

# Now need to exponentiate to work out paths of different lengths (i.e. orbits of different sub-levels)
# Need to work out how to avoid double counting (is this an issue?)
# Need to work out stopping criteria

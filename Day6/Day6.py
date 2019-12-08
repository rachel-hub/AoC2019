# AoC 2019 Day 6

# Packages

import pandas as pd
import numpy as np

# Inputs

InputData = np.loadtxt("aoc2019_day6_input.txt",
                       dtype='str')

# Data prep
# Aim: Get a square adjacency matrix where 1 represents a direct orbit and zero no orbit

# Split the orbits into two columns, one for the centre and one for the thing orbiting
InputData = pd.DataFrame(InputData,
                         columns = ["Input"])

splitInput = InputData["Input"].str.split(")", expand = True)

InputData["Centre"] = splitInput[0]
InputData["Orbiter"] = splitInput[1]

# Create a data frame of distinct planets in the solar system
DistinctPlanets = pd.concat([splitInput[0], splitInput[1]]).unique()
DistinctPlanets = pd.DataFrame(DistinctPlanets,
                               columns = ["Planets"])

# Use the data frame of distinct planets to create a data frame of all pairs of planets
DistinctPlanets["dummy"] = 1
AllPlanets = DistinctPlanets.merge(DistinctPlanets, on="dummy", how="outer")
AllPlanets = AllPlanets.rename(columns={"Planets_x":"Centre", "Planets_y": "Orbiter"})

# Add a column with a 1 for a direct orbit and a 0 for no direct orbit
AllPlanets = AllPlanets.merge(InputData, on = ["Centre", "Orbiter"], how="left")
AllPlanets.loc[pd.notnull(AllPlanets["Input"]), "InOrbit"] = 1
AllPlanets.loc[pd.isnull(AllPlanets["Input"]), "InOrbit"] = 0

# Tidy data, pivot and convert to numpy array ready for matrix multiplication
AllPlanets = AllPlanets[["Centre", "Orbiter", "InOrbit"]]
AllPlanetsPivot = AllPlanets.pivot(index="Centre", columns="Orbiter", values="InOrbit")
AdjacencyMatrix = np.array(AllPlanetsPivot)

# Part 1

# Use mathematical properties of adjacency matrices
# An entry of 1 in A^n means there's a path of length n between those two indices
# Here a path of length n means an indirect orbit n apart
thisMatrix = AdjacencyMatrix.copy()
thisMatrixSum = thisMatrix.sum()
totalOrbits = thisMatrixSum.copy()
i = 2
while thisMatrixSum > 0:
    if (i//50) == (i/50):
        print("Currently on exponent " + str(i))
    thisMatrix = np.matmul(thisMatrix, AdjacencyMatrix)
    thisMatrixSum = thisMatrix.sum()
    totalOrbits += thisMatrixSum
    i += 1

totalOrbits

# Part 2

# We are no longer interested in what orbits what but in travelling between orbits
# Need an adjacency matrix with bidirectional edges
AdjustedAdjacencyMatrix = AdjacencyMatrix + np.transpose(AdjacencyMatrix)

# Work out which index represents "YOU" and which represents "SAN"
SortedPlanets = DistinctPlanets.sort_values(by="Planets").reset_index(drop=True)
MyIndex = SortedPlanets[SortedPlanets["Planets"] == "YOU"].index.tolist()[0]
SantaIndex = SortedPlanets[SortedPlanets["Planets"] == "SAN"].index.tolist()[0]

# When there's a path of length j between me and santa, the entry in the matrix will be 1
# All other times it is zero
CurrentPathMatrix = AdjustedAdjacencyMatrix.copy()
j = 1
while CurrentPathMatrix[MyIndex,SantaIndex] == 0:
    if (j//50) == (j/50):
        print("Currently on exponent " + str(j))
    CurrentPathMatrix = np.matmul(CurrentPathMatrix, AdjustedAdjacencyMatrix)
    j += 1

# But we're not counting from me to santa, we're counting from the nearest things we're orbiting so subtract 2
DistanceToSanta = j - 2

DistanceToSanta

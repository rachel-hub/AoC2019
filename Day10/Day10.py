# AoC 2019 Day 10

# Modules

import numpy as np
import pandas as pd

# Inputs

with open('aoc2019_day10_input.txt', 'r') as f:
    x = f.read().splitlines()

InputData = []
for line in x:
    LineValues = [char for char in line]
    InputData.append(LineValues)

InputData = np.array(InputData)

TestInput1 = [['.','#','.','.','#'],
              ['.','.','.','.','.'],
              ['#','#','#','#','#'],
              ['.','.','.','.','#'],
              ['.','.','.','#','#']]

TestInput1 = np.array(TestInput1)

# In the input, "." denotes and empty position an "#" denotes an asteroid

# Part 1

# ThisInput = TestInput1.copy()
ThisInput = InputData.copy()

asteroids = np.where(ThisInput == '#')

AsteroidCoordinates = []
for k in range(len(asteroids[0])):
    AsteroidCoordinates.append(np.array([asteroids[1][k], asteroids[0][k]]))

# AsteroidCoordinates = np.array(AsteroidCoordinates)

# StartAsteroid = AsteroidCoordinates[0]
# AsteroidDirections = AsteroidCoordinates - StartAsteroid
# SquareAsteroidDirections = np.pad(AsteroidDirections, ((0,0),(0,8)), 'constant', constant_values=(0))
# MyQuadrant4Directions = [x for x in AsteroidDirections if (x[0] >= 0) and (x[1] >= 0)]

# InterestingAsteroidDirections = AsteroidDirections[1:]


def get_number_of_visible_asteroids(asteroid_directions):
    visible_directions = []
    for k in range(len(asteroid_directions)):
        this_asteroid = asteroid_directions[k]
        # print("Now started direction " + str(this_asteroid))
        if (len(visible_directions) == 0) and (abs(this_asteroid).sum() != 0) :
            visible_directions.append(this_asteroid)
            # print("Asteroid added to output because nothing is in it")
        elif abs(this_asteroid).sum() != 0:
            collinear_count = 0
            for kk in range(len(visible_directions)):
                cross_product = np.cross(this_asteroid, visible_directions[kk])
                # print(asteroid_directions[k], visible_directions[kk])
                # print(cross_product)
                if cross_product == 0:
                    collinear_count += 1
            # print(collinear_count)
            if collinear_count == 0:
                visible_directions.append(this_asteroid)
    return len(visible_directions)


BestLocation = []
NumberOfAsteroidsVisible = 0

for AsteroidCoordinate in AsteroidCoordinates:
    print("Current asteroid coordinate is " + str(AsteroidCoordinate))
    AsteroidDirections = AsteroidCoordinates - AsteroidCoordinate
    # InterestingAsteroidDirections = AsteroidDirections[1:]
    Quadrant1Directions = [x for x in AsteroidDirections if (x[0] < 0) and (x[1] < 0)]
    # print("Quadrant 1 directions are " + str(Quadrant1Directions))
    Quadrant2Directions = [x for x in AsteroidDirections if (x[0] < 0) and (x[1] >= 0)]
    # print("Quadrant 2 directions are " + str(Quadrant2Directions))
    Quadrant3Directions = [x for x in AsteroidDirections if (x[0] >= 0) and (x[1] < 0)]
    # print("Quadrant 3 directions are " + str(Quadrant3Directions))
    Quadrant4Directions = [x for x in AsteroidDirections if (x[0] >= 0) and (x[1] >= 0)]
    # print("Quadrant 4 directions are " + str(Quadrant4Directions))

    Quadrant1VisibleAsteroids = get_number_of_visible_asteroids(Quadrant1Directions)
    Quadrant2VisibleAsteroids = get_number_of_visible_asteroids(Quadrant2Directions)
    Quadrant3VisibleAsteroids = get_number_of_visible_asteroids(Quadrant3Directions)
    Quadrant4VisibleAsteroids = get_number_of_visible_asteroids(Quadrant4Directions)

    # print("Quadrant asteroids visible are " + str(Quadrant1VisibleAsteroids) + ", " + str(Quadrant2VisibleAsteroids) + \
    #        ", " + str(Quadrant3VisibleAsteroids) + ", " + str(Quadrant4VisibleAsteroids))

    NumberOfVisibleAsteroids = Quadrant1VisibleAsteroids + Quadrant2VisibleAsteroids + Quadrant3VisibleAsteroids + \
                               Quadrant4VisibleAsteroids
    print(AsteroidCoordinate, NumberOfVisibleAsteroids)
    if NumberOfVisibleAsteroids > NumberOfAsteroidsVisible:
        BestLocation = AsteroidCoordinate
        NumberOfAsteroidsVisible = NumberOfVisibleAsteroids

# Maximum number of asteroids visible is 267
# This occurs at [26, 28]

# Part 2

# Asteroid station on [26,28]

VectorsToAsteroidStation = AsteroidCoordinates - np.array(BestLocation)
DistancesToAsteroids = [np.sqrt(x.dot(x)) for x in VectorsToAsteroidStation]

UnitVector = np.array([1, 0])
CrossProducts = [np.cross(x, UnitVector) for x in VectorsToAsteroidStation]
DotProducts = [np.dot(x, UnitVector) for x in VectorsToAsteroidStation]

SineAngles = []
CosineAngles = []
for k in range(len(DistancesToAsteroids)):
    if DistancesToAsteroids != 0:
        SineAngles += [CrossProducts[k]/DistancesToAsteroids[k]]
        CosineAngles += [DotProducts[k]/DistancesToAsteroids[k]]
    else:
        SineAngles += [0]
        CosineAngles += [0]

AsteroidXCoordinates = [x[0] for x in AsteroidCoordinates]
AsteroidYCoordinates = [x[1] for x in AsteroidCoordinates]

AsteroidZappingInfo = pd.DataFrame({"x_coord": AsteroidXCoordinates,
                                    "y_coord": AsteroidYCoordinates,
                                    "distance": DistancesToAsteroids,
                                    "sine": SineAngles,
                                    "cosine": CosineAngles})

AsteroidZappingInfo["arcsine"] = np.arcsin(AsteroidZappingInfo["sine"])
AsteroidZappingInfo["arccosine"] = np.arcsin(AsteroidZappingInfo["cosine"])

AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] > 0) & (AsteroidZappingInfo["cosine"] > 0),
                                        AsteroidZappingInfo["arcsine"], np.nan)
AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] > 0) & (AsteroidZappingInfo["cosine"] <= 0),
                                        AsteroidZappingInfo["arccosine"], AsteroidZappingInfo["angle"])
AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] <= 0) & (AsteroidZappingInfo["cosine"] <= 0),
                                        AsteroidZappingInfo["arccosine"], AsteroidZappingInfo["angle"])
AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] <= 0) & (AsteroidZappingInfo["cosine"] > 0),
                                        AsteroidZappingInfo["arccosine"], AsteroidZappingInfo["angle"])

# Need to work out what the cases for getting angles should be here so they are all in the interval [0,2*pi)
# Need to ensure this is set-up with the right unit vector so zero is in the right place
# Need to handle the value that is the monitoring station
# Then order by angle then distance
# Work out what the minimum difference between angles is
# Work through looking for the next one that is least as big a difference than that is (or more than half distance)
# Remove values from data frame as we loop
# Put into a for loop so 200th thing can be returned

# AoC 2019 Day 10

# Modules

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 10)

# Inputs

with open('aoc2019_day10_input.txt', 'r') as f:
    x = f.read().splitlines()

# with open('aoc2019_day10_input_big_example.txt', 'r') as f:
#     x = f.read().splitlines()

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

# Create 2D vectors to the asteroid station
VectorsToAsteroidStation = AsteroidCoordinates - np.array(BestLocation)
# Use dot product to get distances between the asteroid station and all asterois (including the one it is on)
DistancesToAsteroids = [np.sqrt(x.dot(x)) for x in VectorsToAsteroidStation]

# Define a unit vector that points straight up
# This is where the lazer should start
UnitVector = np.array([0, -1])

# Calculate cross products and dot products with our unit vector
# We can use these to get cosines and sines relative to straight up which we can calculate angles from
CrossProducts = [np.cross(x, UnitVector) for x in VectorsToAsteroidStation]
DotProducts = [np.dot(x, UnitVector) for x in VectorsToAsteroidStation]

# Create lists of sine and cosine angles to the unit vector
# Handle the exception of the monitoring station which is at zero distance by infilling zero
# This choice doesn't really matter - we will exclude it based upon distance later
SineAngles = []
CosineAngles = []
for k in range(len(DistancesToAsteroids)):
    if DistancesToAsteroids[k] != 0:
        SineAngles += [CrossProducts[k]/DistancesToAsteroids[k]]
        CosineAngles += [DotProducts[k]/DistancesToAsteroids[k]]
    else:
        SineAngles += [0]
        CosineAngles += [0]

# Separate out x and y co-ordinates
# Then they can be one column each in our data frame
AsteroidXCoordinates = [x[0] for x in AsteroidCoordinates]
AsteroidYCoordinates = [x[1] for x in AsteroidCoordinates]

# Create a data frame of the asteroids and the information relative to the monitoring station
AsteroidZappingInfo = pd.DataFrame({"x_coord": AsteroidXCoordinates,
                                    "y_coord": AsteroidYCoordinates,
                                    "distance": DistancesToAsteroids,
                                    "sine": SineAngles,
                                    "cosine": CosineAngles})

# Calculate arcsine and arccosine to help recover angle between asteroid and our unit vector
AsteroidZappingInfo["arcsine"] = np.arcsin(AsteroidZappingInfo["sine"])
AsteroidZappingInfo["arccosine"] = np.arccos(AsteroidZappingInfo["cosine"])

# Four cases to recover angles for each of the four quadrants
AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] > 0) & (AsteroidZappingInfo["cosine"] > 0),
                                        AsteroidZappingInfo["arcsine"], np.nan)
AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] > 0) & (AsteroidZappingInfo["cosine"] <= 0),
                                        AsteroidZappingInfo["arccosine"], AsteroidZappingInfo["angle"])
AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] <= 0) & (AsteroidZappingInfo["cosine"] <= 0),
                                        np.pi - AsteroidZappingInfo["arcsine"], AsteroidZappingInfo["angle"])
AsteroidZappingInfo["angle"] = np.where((AsteroidZappingInfo["sine"] <= 0) & (AsteroidZappingInfo["cosine"] > 0),
                                        2*np.pi - AsteroidZappingInfo["arccosine"], AsteroidZappingInfo["angle"])

# Subtract angles from 2pi to get clockwise rotation
AsteroidZappingInfo["angle"] = 2*np.pi - AsteroidZappingInfo["angle"]

# Round angles to 12dp to eliminate floating point errors - need to be able to test angle equality
AsteroidZappingInfo["angle"] = np.round(AsteroidZappingInfo["angle"], 12)

# Check all angles in range [0, 2pi)
AsteroidZappingInfo.angle.min() >= 0
AsteroidZappingInfo.angle.max() < 2*np.pi

# Work out where our monitoring station is
MonitoringStationIndex = AsteroidZappingInfo[AsteroidZappingInfo["distance"] == 0].index[0]
# len(AsteroidZappingInfo)

# Remove our monitoring station from our list of asteroids to be zapped
AsteroidZappingInfo.drop(index=MonitoringStationIndex, inplace=True)
# len(AsteroidZappingInfo)

# Work through angles, zapping closes asteroid an moving to the next closest angle
# Start at angle zero (straight up)
ReferenceAngle = 0

for k in range(200):
    print("This is asteroid " + str(k) + " being zapped.")
    # The asteroid that's zapped is the one closest to but beyond our reference angle
    ZappingAngle = AsteroidZappingInfo[AsteroidZappingInfo["angle"] >= ReferenceAngle].angle.min()
    print(ZappingAngle)
    # If there are multiple asteroids at that angle, zap the one at the closest distance
    DistanceToClosestAsteroid = AsteroidZappingInfo[AsteroidZappingInfo["angle"] == ReferenceAngle].distance.min()
    print(DistanceToClosestAsteroid)
    # Get the data frame index for the asteroid to be zapped so we can remove it from our asteroid data
    ZappingIndex = AsteroidZappingInfo[(AsteroidZappingInfo["angle"] == ZappingAngle) &
                                       (AsteroidZappingInfo["distance"] == DistanceToClosestAsteroid)].index[0]
    # Store information about what is soon to be our most recently zapped asteroid
    LastAsteroidZapped = AsteroidZappingInfo.loc[ZappingIndex,]
    print("Asteroid zapped is " + str(LastAsteroidZapped["x_coord"]) + ", " + str(LastAsteroidZapped["y_coord"]))
    # Zap the asteroid by removing it from our asteroid data
    AsteroidZappingInfo.drop(index=ZappingIndex, inplace=True)
    # Update the reference angle so the lazer rotates
    ReferenceAngle = AsteroidZappingInfo[AsteroidZappingInfo["angle"] > ReferenceAngle].angle.min()
    # If we go past the largest angle, reset the reference angle to zero so another rotation occurs
    if np.isnan(ReferenceAngle):
        ReferenceAngle = 0

# Calculate the required output
LastXCoord = LastAsteroidZapped["x_coord"]
LastYCoord = LastAsteroidZapped["y_coord"]

OutputPart2 = 100*LastXCoord + LastYCoord

OutputPart2
# This is 1309

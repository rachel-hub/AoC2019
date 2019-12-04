# AoC 2019 Day 3

# Import modules
import numpy as np

# Inputs

InputData = np.loadtxt("aoc2019_day3_input.txt",
                       dtype=str)

TestData = np.array(["R8,U5,L5,D3",
                     "U7,R6,D4,L4"])

# Functions


def generate_wire_coordinates(wire):
    coordinates = []
    x_coordinate = 0
    y_coordinate = 0

    for path_id in wire:
        path_direction = path_id[0]
        path_step = int(path_id[1:])
        if path_direction == "L":
            for k in range(1, path_step+1):
                x_coordinate -= 1
                coordinates.append((x_coordinate, y_coordinate))
        elif path_direction == "R":
            for k in range(1, path_step+1):
                x_coordinate += 1
                coordinates.append((x_coordinate, y_coordinate))
        elif path_direction == "U":
            for k in range(1, path_step+1):
                y_coordinate += 1
                coordinates.append((x_coordinate, y_coordinate))
        elif path_direction == "D":
            for k in range(1, path_step+1):
                y_coordinate -= 1
                coordinates.append((x_coordinate, y_coordinate))
        else:
            print("Unknown path direction")
            break

    return coordinates


# Part 1

Wire1 = InputData[0].split(",")
Wire2 = InputData[1].split(",")

# Wire1 = TestData[0].split(",")
# Wire2 = TestData[1].split(",")

Wire1Coordinates = generate_wire_coordinates(Wire1)
Wire2Coordinates = generate_wire_coordinates(Wire2)

# Calculate wire intersections

WireOverlaps = list(set(Wire1Coordinates) & set(Wire2Coordinates))

WireDistances = [abs(coordinate_pair[0]) + abs(coordinate_pair[1]) for coordinate_pair in WireOverlaps]

# Identify which is the shortest Manhattan distance intersection
result = min(WireDistances)
# result = WireOverlaps[WireDistances.index(min(WireDistances))]

# Part 2

# Need to calculate minimum signal delay

# Need to add 2 because 1 needs addingto each index due to zero based indexing
SignalDelay = [Wire1Coordinates.index(overlap) + Wire2Coordinates.index(overlap) + 2 for overlap in WireOverlaps]

minDelay = min(SignalDelay)

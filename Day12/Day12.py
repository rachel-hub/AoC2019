# Aoc 2019 Day 12

# modules

import numpy as np

# Input

# Input in the form given
# <x=14, y=4, z=5>
# <x=12, y=10, z=8>
# <x=1, y=7, z=-10>
# <x=16, y=-5, z=3>

PositionI = np.array([14, 4, 5])
PositionE = np.array([12, 10, 8])
PositionG = np.array([1, 7, -10])
PositionC = np.array([16, -5, 3])

# Test Input

# Input in the form given
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>

# PositionI = np.array([-1, 0, 2])
# PositionE = np.array([2, -10, -7])
# PositionG = np.array([4, -8, 8])
# PositionC = np.array([3, 5, -1])

VelocityI = np.array([0,0,0])
VelocityE = np.array([0,0,0])
VelocityG = np.array([0,0,0])
VelocityC = np.array([0,0,0])


# Part 1

def get_gravity(position_moon_a, position_moon_b):
    gravity_moon_a = -1*(position_moon_a > position_moon_b) + 1*(position_moon_a < position_moon_b)
    return gravity_moon_a


def get_potential_energy(moon_position):
    potential_energy = np.abs(moon_position).sum()
    return potential_energy


def get_kinetic_energy(moon_velocity):
    kinetic_energy = np.abs(moon_velocity).sum()
    return kinetic_energy


for k in range(1000):
    GravityI = get_gravity(PositionI, PositionE) + get_gravity(PositionI, PositionG) + get_gravity(PositionI, PositionC)
    GravityE = get_gravity(PositionE, PositionI) + get_gravity(PositionE, PositionG) + get_gravity(PositionE, PositionC)
    GravityG = get_gravity(PositionG, PositionI) + get_gravity(PositionG, PositionE) + get_gravity(PositionG, PositionC)
    GravityC = get_gravity(PositionC, PositionI) + get_gravity(PositionC, PositionE) + get_gravity(PositionC, PositionG)

    VelocityI += GravityI
    VelocityE += GravityE
    VelocityG += GravityG
    VelocityC += GravityC

    PositionI += VelocityI
    PositionE += VelocityE
    PositionG += VelocityG
    PositionC += VelocityC

EnergyI = get_potential_energy(PositionI) * get_kinetic_energy(VelocityI)
EnergyE = get_potential_energy(PositionE) * get_kinetic_energy(VelocityE)
EnergyG = get_potential_energy(PositionG) * get_kinetic_energy(VelocityG)
EnergyC = get_potential_energy(PositionC) * get_kinetic_energy(VelocityC)

TotalEnergy = EnergyI + EnergyE + EnergyG + EnergyC

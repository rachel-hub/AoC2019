# AoC 2019 Day 2

# Packages

import numpy as np

# Inputs

InputData = np.loadtxt("aoc2019_day2_input.txt",
                       dtype='int64',
                       delimiter=",")

# Copied from AoC webpage
TestInput = np.array([1,9,10,3,2,3,11,0,99,30,40,50])

# About intcode programs:
# Intcode programs are given as a list of integers;
# these values are used as the initial state for the computer's memory.
# When you run an Intcode program, make sure to start by initializing memory to the program's values.
# A position in memory is called an address (for example, the first value in memory is at "address 0").
#
# Opcodes (like 1, 2, or 99) mark the beginning of an instruction.
# The values used immediately after an opcode, if any, are called the instruction's parameters.
# For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4 are the parameters.
# The instruction 99 contains only an opcode and has no parameters.
#
# The address of the current instruction is called the instruction pointer; it starts at 0.
# After an instruction finishes, the instruction pointer increases by the number of values in the instruction;
# until you add more instructions to the computer,
# this is always 4 (1 opcode + 3 parameters) for the add and multiply instructions.
# (The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)

# Define the intcode program
# In the below;
#   input_data is the initial memory state
#   this_input tracks what is in the memory
#   current_index is the instruction pointer
#   index1, index2 and insert_index are the parameters

# It might be sensible to parametrise by the number of parameters to help future proof


def intcode(input_data,noun,verb):
    this_input = input_data.copy()
    current_index = 0
    current_op_code = this_input[current_index].copy()

    this_input[1] = noun
    this_input[2] = verb

    while current_op_code != 99:
        if current_op_code == 1:
            # print("OpCode identified as 1")
            index1 = this_input[current_index + 1]
            index2 = this_input[current_index + 2]
            sum_val = this_input[index1] + this_input[index2]
            insert_index = this_input[current_index + 3]
            this_input[insert_index] = sum_val
            current_index += 4
            current_op_code = this_input[current_index].copy()

        elif current_op_code == 2:
            # print("OpCode identified as 2")
            index1 = this_input[current_index + 1]
            index2 = this_input[current_index + 2]
            mult_val = this_input[index1] * this_input[index2]
            insert_index = this_input[current_index + 3]
            this_input[insert_index] = mult_val
            current_index += 4
            current_op_code = this_input[current_index].copy()

        else:
            print("Unknown OpCode identified")
            break

    return this_input[0]


# Part 1

print(intcode(InputData,12,2))

# Part 2
# Loop through noun and verb values until we get our match

for noun_val in range(100):
    for verb_val in range(100):
        output = intcode(InputData,noun_val,verb_val)
        if output == 19690720:
            break
    if output == 19690720:
        break

print(100*noun_val + verb_val)

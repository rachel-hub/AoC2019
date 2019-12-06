# AoC 2019 Day 5

# Packages

import numpy as np

# Inputs

InputData = np.loadtxt("aoc2019_day5_input.txt",
                       dtype='int64',
                       delimiter=",")


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
#   input is an input parameter value

# It might be sensible to parametrise by the number of parameters to help future proof


def intcode(input_data,input):
    this_input = input_data.copy()
    current_index = 0
    max_index = len(this_input) - 1
    current_op_mode_code = this_input[current_index].copy()
    current_mode_codes = current_op_mode_code // 100
    current_op_code = current_op_mode_code - current_mode_codes * 100
    current_mode_code_3 = current_mode_codes // 100
    current_mode_code_2 = (current_mode_codes - current_mode_code_3 * 100) // 10
    current_mode_code_1 = (current_mode_codes - current_mode_code_3 * 100 - current_mode_code_2 * 10)

    # Check mode codes are valid
    if not((current_mode_code_1 == 0) or (current_mode_code_1 == 1)):
        return "Error with mode code 1"
    if not((current_mode_code_2 == 0) or (current_mode_code_2 == 1)):
        return "Error with mode code 2"
    if not((current_mode_code_3 == 0) or (current_mode_code_3 == 1)):
        return "Error with mode code 3"

    while current_op_code != 99:
        current_op_mode_code = this_input[current_index].copy()
        current_mode_codes = current_op_mode_code // 100
        current_op_code = current_op_mode_code - current_mode_codes * 100
        current_mode_code_3 = current_mode_codes // 100
        current_mode_code_2 = (current_mode_codes - current_mode_code_3 * 100) // 10
        current_mode_code_1 = (current_mode_codes - current_mode_code_3 * 100 - current_mode_code_2 * 10)

        if current_op_code == 99:
            return "Halt"

        # Check mode codes are valid
        if not ((current_mode_code_1 == 0) or (current_mode_code_1 == 1)):
            return "Error with mode code 1"
        if not ((current_mode_code_2 == 0) or (current_mode_code_2 == 1)):
            return "Error with mode code 2"
        if not ((current_mode_code_3 == 0) or (current_mode_code_3 == 1)):
            return "Error with mode code 3"

        index1 = this_input[current_index + 1]
        index2 = this_input[current_index + 2]
        insert_index = this_input[current_index + 3]

        try:
            parameter1 = (1 - current_mode_code_1)*this_input[min(max(0,index1),max_index)] + current_mode_code_1*index1
        except:
            pass
        try:
            parameter2 = (1 - current_mode_code_2)*this_input[min(max(0,index2),max_index)] + current_mode_code_2*index2
        except:
            pass

        if current_op_code == 1:
            # print("OpCode identified as 1")
            sum_val = parameter1 + parameter2
            this_input[insert_index] = sum_val
            current_index += 4

        elif current_op_code == 2:
            # print("OpCode identified as 2")
            mult_val = parameter1 * parameter2
            this_input[insert_index] = mult_val
            current_index += 4

        elif current_op_code == 3:
            this_input[index1] = input
            current_index += 2

        elif current_op_code == 4:
            print(parameter1)
            current_index += 2

        elif current_op_code == 5:
            if parameter1 != 0:
                current_index = parameter2
            else:
                current_index += 3

        elif current_op_code == 6:
            if parameter1 == 0:
                current_index = parameter2
            else:
                current_index += 3

        elif current_op_code == 7:
            if parameter1 < parameter2:
                this_input[insert_index] = 1
            else:
                this_input[insert_index] = 0
            current_index += 4

        elif current_op_code == 8:
            if parameter1 == parameter2:
                this_input[insert_index] = 1
            else:
                this_input[insert_index] = 0
            current_index += 4

        else:
            print(current_op_code)
            print("Unknown OpCode identified")
            break


# Part 1

intcode(InputData,1)

# Part 2

intcode(InputData,5)

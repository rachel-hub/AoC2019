# AoC 2019 Day 7

# Packages

import numpy as np

# Inputs

InputData = np.loadtxt("aoc2019_day9_input.txt",
                       dtype='int64',
                       delimiter=",").tolist()


TestData1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# TestData1 takes no input and produces a copy of itself as output.
TestData2 = [1102,34915192,34915192,7,4,7,99,0]
# TestData2 should output a 16-digit number.
TestData3 = [104,1125899906842624,99]
# TestData3 should output the large number in the middle.

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


def intcode(input_data, input_value, current_index=0, relative_base=0, return_value=np.nan):
    this_input = input_data.copy()
    # max_index = len(this_input) - 1
    # current_op_mode_code = this_input[current_index]
    # current_mode_codes = current_op_mode_code // 100
    # current_op_code = current_op_mode_code - current_mode_codes * 100
    # current_mode_code_3 = current_mode_codes // 100
    # current_mode_code_2 = (current_mode_codes - current_mode_code_3 * 100) // 10
    # current_mode_code_1 = (current_mode_codes - current_mode_code_3 * 100 - current_mode_code_2 * 10)
    #
    # # Check mode codes are valid
    # if not((current_mode_code_1 == 0) or (current_mode_code_1 == 1) or (current_mode_code_1 == 2)):
    #     return "Error with mode code 1"
    # if not((current_mode_code_2 == 0) or (current_mode_code_2 == 1) or (current_mode_code_2 == 2)):
    #     return "Error with mode code 2"
    # if not((current_mode_code_3 == 0) or (current_mode_code_3 == 1) or (current_mode_code_3 == 2)):
    #     return "Error with mode code 3"

    while True:
        max_index = len(this_input) - 1
        print("Curent index is " + str(current_index))
        try:
            current_op_mode_code = this_input[current_index]
        except:
            this_input += [0 for k in range(current_index + 1 - max_index)]
            current_op_mode_code = this_input[current_index]

        print("Current Op Mode code is " + str(current_op_mode_code))

        current_mode_codes = current_op_mode_code // 100
        # print("Current Mode codes are " + str(current_mode_codes))
        current_op_code = current_op_mode_code - current_mode_codes * 100
        current_mode_code_3 = current_mode_codes // 100
        current_mode_code_2 = (current_mode_codes - current_mode_code_3 * 100) // 10
        current_mode_code_1 = (current_mode_codes - current_mode_code_3 * 100 - current_mode_code_2 * 10)

        # print("Mode code 1 is " + str(current_mode_code_1))
        # print("Mode code 2 is " + str(current_mode_code_2))
        # print("Mode code 3 is " + str(current_mode_code_3))

        # Check mode codes are valid
        if not ((current_mode_code_1 == 0) or (current_mode_code_1 == 1) or (current_mode_code_1 == 2)):
            return "Error with mode code 1"
        if not ((current_mode_code_2 == 0) or (current_mode_code_2 == 1) or (current_mode_code_2 == 2)):
            return "Error with mode code 2"
        if not ((current_mode_code_3 == 0) or (current_mode_code_3 == 1) or (current_mode_code_3 == 2)):
            return "Error with mode code 3"

        try:
            index1 = this_input[current_index + 1]
        except:
            this_input += [0]
            index1 = this_input[current_index + 1]

        try:
            index2 = this_input[current_index + 2]
        except:
            this_input += [0]
            index2 = this_input[current_index + 2]

        if (current_mode_code_1 == 0) and (current_op_code != 99):
            try:
                parameter1 = this_input[max(0, index1)]
            except:
                this_input += [0 for k in range(index1 + 1 - len(this_input))]
                parameter1 = this_input[max(0, index1)]

        elif (current_mode_code_1 == 1) and (current_op_code != 99):
            parameter1 = index1

        elif (current_mode_code_1 == 2) and (current_op_code != 99):
            try:
                parameter1 = this_input[max(0, index1 + relative_base)]
            except:
                this_input += [0 for k in range(index1 + relative_base + 1 - len(this_input))]
                parameter1 = this_input[max(0, index1 + relative_base)]

        if (current_mode_code_2 == 0) and (current_op_code in [1,2,5,6,7,8]):
            try:
                parameter2 = this_input[max(0, index2)]
            except:
                # print("Current mode code is " + str(current_mode_code_2))
                # print("Index2 is " + str(index2))
                # print("Memory length before adjustment is " + str(len(this_input)))
                this_input += [0 for k in range(index2 + 1 - len(this_input))]
                # print("Memory length after adjustment is " + str(len(this_input)))
                parameter2 = this_input[max(0, index2)]

        elif (current_mode_code_2 == 1) and (current_op_code in [1,2,5,6,7,8]):
            parameter2 = index2

        elif (current_mode_code_2 == 2) and (current_op_code in [1,2,5,6,7,8]):
            try:
                parameter2 = this_input[max(0, index2 + relative_base)]
            except:
                this_input += [0 for k in range(index2 + relative_base + 1 - len(this_input))]
                parameter2 = this_input[max(0, index2 + relative_base)]

        if (current_mode_code_3 == 0) and (current_op_code in [1,2,7,8]):
            try:
                insert_index = this_input[current_index + 3]
            except:
                this_input += [0]
                insert_index = this_input[current_index + 3]
            if insert_index > (len(this_input) -1):
                this_input += [0 for k in range(insert_index + 1 - len(this_input))]

        # Never have mode code 3 as 1 because the third parameter is always about insertion

        if (current_mode_code_3 == 2) and (current_op_code in [1,2,7,8]):
            try:
                insert_index = this_input[current_index + 3] + relative_base
            except:
                this_input += [0 for k in range(current_index + 4 - len(this_input))]
                insert_index = this_input[current_index + 3] + relative_base
            if insert_index > (len(this_input) -1):
                this_input += [0 for k in range(insert_index + 1 - len(this_input))]

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
            if current_mode_code_1 == 0:
                this_input[index1] = input_value
            elif current_mode_code_1 == 2:
                this_input[index1 + relative_base] = input_value
            current_index += 2

        elif current_op_code == 4:
            print(parameter1)
            return_value = parameter1
            current_index += 2
            return return_value, current_op_code, current_index, relative_base, this_input

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

        elif current_op_code == 9:
            relative_base += parameter1
            current_index += 2

        elif current_op_code == 99:
            return return_value, current_op_code

        else:
            print(current_op_code)
            print(current_op_code == 99)
            print("Unknown OpCode identified")
            break


def complete_intcode_runner(input_data, input_value, relative_base=0):
    outputs =  intcode(input_data, input_value, relative_base=relative_base)
    while outputs[1] != 99:
        outputs = intcode(outputs[4], outputs[0], outputs[2], outputs[3], outputs[0])
    return outputs[0]


# Inputs: input_data, input_value, current_index = 0, relative_base = 0, return_value = np.nan
# Outputs: return_value, current_op_code, current_index, relative_base, this_input

# Test cases

# TestOutput1 = complete_intcode_runner(TestData1, np.nan)
# TestOutput2 = complete_intcode_runner(TestData2, np.nan)
# TestOutput3 = complete_intcode_runner(TestData3, np.nan)

# Part 1

Part1Output = complete_intcode_runner(InputData,1)

# Part 2

Part2Output = complete_intcode_runner(InputData,2)

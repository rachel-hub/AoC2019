# AoC 2019 Day 7

# Packages

import numpy as np
from itertools import permutations

# Inputs

InputData = np.loadtxt("aoc2019_day7_input.txt",
                       dtype='int64',
                       delimiter=",")

# TestInput1 = np.array([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
# InputData = TestInput1.copy()


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


def intcode(input_data,phase_value,input_value,return_value = np.nan,phase_use_counter = 0,current_index = 0):
    this_input = input_data.copy()
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
            return return_value

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
            if phase_use_counter == 0:
                this_input[index1] = phase_value
                phase_use_counter += 1
            else:
                this_input[index1] = input_value
            current_index += 2

        elif current_op_code == 4:
            print(parameter1)
            return_value = parameter1.copy()
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


def intcode2(input_data,phase_value,input_value,return_value = np.nan,phase_use_counter = 0,current_index = 0):
    this_input = input_data.copy()
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

        # Check mode codes are valid
        if not ((current_mode_code_1 == 0) or (current_mode_code_1 == 1)):
            return "Error with mode code 1"
        if not ((current_mode_code_2 == 0) or (current_mode_code_2 == 1)):
            return "Error with mode code 2"
        if not ((current_mode_code_3 == 0) or (current_mode_code_3 == 1)):
            return "Error with mode code 3"

        index1 = this_input[current_index + 1]
        index2 = this_input[current_index + 2]
        try:
            insert_index = this_input[current_index + 3]
        except:
            pass

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
            if phase_use_counter == 0:
                this_input[index1] = phase_value
                phase_use_counter += 1
            else:
                this_input[index1] = input_value
            current_index += 2

        elif current_op_code == 4:
            print(parameter1)
            return_value = parameter1.copy()
            current_index += 2
            return return_value, current_op_code, current_index, phase_use_counter, this_input

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

    if current_op_code == 99:
        return return_value, current_op_code


def complete_intcode2_runner(input_data,phase_value,input_value):
    outputs =  intcode2(input_data,phase_value,input_value)
    while outputs[1] != 99:
        outputs = intcode2(outputs[4],phase_value,outputs[0],outputs[0],outputs[3],outputs[2])
    return outputs[0]




def amplifiers(input_data,phase_value_a,phase_value_b,phase_value_c,phase_value_d,phase_value_e,input_value):
    amplifier_a_value = intcode(input_data, phase_value_a, input_value)
    amplifier_b_value = intcode(input_data, phase_value_b, amplifier_a_value)
    amplifier_c_value = intcode(input_data, phase_value_c, amplifier_b_value)
    amplifier_d_value = intcode(input_data, phase_value_d, amplifier_c_value)
    amplifier_e_value = intcode(input_data, phase_value_e, amplifier_d_value)
    return amplifier_e_value


def amplifiers2(input_data,phase_value_a,phase_value_b,phase_value_c,phase_value_d,phase_value_e,input_value):
    amplifier_a_value = complete_intcode2_runner(input_data, phase_value_a, input_value)
    print(amplifier_a_value)
    amplifier_b_value = complete_intcode2_runner(input_data, phase_value_b, amplifier_a_value)
    amplifier_c_value = complete_intcode2_runner(input_data, phase_value_c, amplifier_b_value)
    amplifier_d_value = complete_intcode2_runner(input_data, phase_value_d, amplifier_c_value)
    amplifier_e_value = complete_intcode2_runner(input_data, phase_value_e, amplifier_d_value)
    return amplifier_e_value

def adjusted_amplifiers(input_data,phase_value_a,phase_value_b,phase_value_c,phase_value_d,phase_value_e,input_value):
    amplifier_a_opcode = 0
    amplifier_b_opcode = 0
    amplifier_c_opcode = 0
    amplifier_d_opcode = 0
    amplifier_e_opcode = 0

    amplifier_a_state = (input_value, amplifier_a_opcode, 0, 0, input_data)
    amplifier_b_state = (input_value, amplifier_b_opcode, 0, 0, input_data)
    amplifier_c_state = (input_value, amplifier_c_opcode, 0, 0, input_data)
    amplifier_d_state = (input_value, amplifier_d_opcode, 0, 0, input_data)
    amplifier_e_state = (input_value, amplifier_e_opcode, 0, 0, input_data)

    amplifier_a_parameters = [input_value]
    amplifier_b_parameters = []
    amplifier_c_parameters = []
    amplifier_d_parameters = []
    amplifier_e_parameters = []

    while (amplifier_a_opcode != 99) or (amplifier_b_opcode != 99) or (amplifier_c_opcode != 99) or \
        (amplifier_d_opcode != 99) or (amplifier_e_opcode != 99):
        if len(amplifier_a_parameters) > 0:
            print("It's amplifier a with opcode " + str(amplifier_a_opcode))

            if amplifier_a_opcode == 99:
                print(amplifier_a_parameters)
                print(amplifier_b_parameters)
                break

            this_parameter = amplifier_a_parameters[0]
            amplifier_a_outputs = intcode2(amplifier_a_state[4], phase_value_a, this_parameter, this_parameter,
                                           amplifier_a_state[3], amplifier_a_state[2])
            amplifier_a_state = amplifier_a_outputs
            if (amplifier_a_state[1] != 99) and (amplifier_a_state[3] > 0):
                amplifier_a_parameters = amplifier_a_parameters[1:]
            amplifier_a_opcode = amplifier_a_outputs[1]
            amplifier_b_parameters.append(amplifier_a_outputs[0])

        if len(amplifier_b_parameters) > 0:
            print("It's amplifier b with opcode " + str(amplifier_b_opcode))
            this_parameter = amplifier_b_parameters[0]
            amplifier_b_outputs = intcode2(amplifier_b_state[4], phase_value_b, this_parameter, this_parameter,
                                           amplifier_b_state[3], amplifier_b_state[2])
            amplifier_b_state = amplifier_b_outputs
            if (amplifier_b_state[1] != 99) and (amplifier_b_state[3] > 0):
                amplifier_b_parameters = amplifier_b_parameters[1:]
            amplifier_b_opcode = amplifier_b_outputs[1]
            amplifier_c_parameters.append(amplifier_b_outputs[0])

        if len(amplifier_c_parameters) > 0:
            print("It's amplifier c with opcode " + str(amplifier_c_opcode))
            this_parameter = amplifier_c_parameters[0]
            amplifier_c_outputs = intcode2(amplifier_c_state[4], phase_value_c, this_parameter, this_parameter,
                                           amplifier_c_state[3], amplifier_c_state[2])
            amplifier_c_state = amplifier_c_outputs
            if (amplifier_c_state[1] != 99) and (amplifier_c_state[3] > 0):
                amplifier_c_parameters = amplifier_c_parameters[1:]
            amplifier_c_opcode = amplifier_c_outputs[1]
            amplifier_d_parameters.append(amplifier_c_outputs[0])

        if len(amplifier_d_parameters) > 0:
            print("It's amplifier d with opcode " + str(amplifier_d_opcode))
            this_parameter = amplifier_d_parameters[0]
            amplifier_d_outputs = intcode2(amplifier_d_state[4], phase_value_d, this_parameter, this_parameter,
                                           amplifier_d_state[3], amplifier_d_state[2])
            amplifier_d_state = amplifier_d_outputs
            if (amplifier_d_state[1] != 99) and (amplifier_d_state[3] > 0):
                amplifier_d_parameters = amplifier_d_parameters[1:]
            amplifier_d_opcode = amplifier_d_outputs[1]
            amplifier_e_parameters.append(amplifier_d_outputs[0])


        if len(amplifier_e_parameters) > 0:
            print("It's amplifier e with opcode " + str(amplifier_e_opcode))
            this_parameter = amplifier_e_parameters[0]
            amplifier_e_outputs = intcode2(amplifier_e_state[4], phase_value_e, this_parameter, this_parameter,
                                           amplifier_e_state[3], amplifier_e_state[2])
            amplifier_e_state  = amplifier_e_outputs
            if (amplifier_e_state[1] != 99) and (amplifier_e_state[3] > 0):
                amplifier_e_parameters = amplifier_e_parameters[1:]
            amplifier_e_opcode = amplifier_e_outputs[1]
            amplifier_a_parameters.append(amplifier_e_outputs[0])
            amplifier_e_value = amplifier_e_outputs[0]

    return amplifier_e_value


# Part 1
# Work out which permutation of phases gives the largest amplifier signal

perms = permutations([0,1,2,3,4])
MaxOutputSignal = 0

for perm in perms:
    phase_a = perm[0]
    phase_b = perm[1]
    phase_c = perm[2]
    phase_d = perm[3]
    phase_e = perm[4]
    output_signal = amplifiers(InputData,phase_a,phase_b,phase_c,phase_d,phase_e,0)
    if output_signal > MaxOutputSignal:
        MaxOutputSignal = output_signal.copy()
        MaxPermutation = perm

MaxOutputSignal

perms2 = permutations([0,1,2,3,4])
MaxOutputSignal2 = 0

for perm in perms2:
    phase_a = perm[0]
    phase_b = perm[1]
    phase_c = perm[2]
    phase_d = perm[3]
    phase_e = perm[4]
    print(phase_a,phase_b,phase_c,phase_d,phase_e)
    output_signal2 = amplifiers2(InputData,phase_a,phase_b,phase_c,phase_d,phase_e,0)
    if output_signal2 > MaxOutputSignal2:
        MaxOutputSignal2 = output_signal2.copy()
        MaxPermutation2 = perm

MaxOutputSignal2

# Part 2

# Intcode2 now is running and gives sensible output for part1
# Try using this for part2 - adjusted_amplifiers is a preliminary structure, just needs testing and debugging

# General thoughts on approach:

# Append output to lists, check their length run non-zero list and depend from the the input used
# Need to handle passing parameters between intcode and others
# Probably want to return values after step 4 with some other parameters to help it resume
# Likely all those set at the start - put them in as inputs with default values instead
# Need to make sure the final return is distinguishable to help with while loop in amplifier handling code

perms3 = permutations([5,6,7,8,9])
MaxOutputSignal3 = 0

for perm in perms3:
    phase_a = perm[0]
    phase_b = perm[1]
    phase_c = perm[2]
    phase_d = perm[3]
    phase_e = perm[4]
    print(phase_a,phase_b,phase_c,phase_d,phase_e)
    output_signal3 = adjusted_amplifiers(InputData,phase_a,phase_b,phase_c,phase_d,phase_e,0)
    if output_signal3 > MaxOutputSignal3:
        MaxOutputSignal3 = output_signal3.copy()
        MaxPermutation3 = perm

MaxOutputSignal3

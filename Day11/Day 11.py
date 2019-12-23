# AoC 2019 Day 11

# Packages

import numpy as np
import matplotlib.pyplot as plt

# Inputs

InputData = np.loadtxt("aoc2019_day11_input.txt",
                       dtype='int64',
                       delimiter=",").tolist()


def intcode(input_data, input_value, current_index=0, relative_base=0, return_value=np.nan):
    this_input = input_data.copy()

    while True:
        max_index = len(this_input) - 1
        # print("Curent index is " + str(current_index))
        try:
            current_op_mode_code = this_input[current_index]
        except:
            this_input += [0 for k in range(current_index + 1 - max_index)]
            current_op_mode_code = this_input[current_index]

        # print("Current Op Mode code is " + str(current_op_mode_code))

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


def spaceship_painter(input_data, input_value=0, relative_base=0):
    # Initialise output counters
    painted_panel_count = 0
    white_panels = []
    distinct_painted_panel_count = 0
    painted_panels = []
    current_panel_colour = input_value
    # Initialise position and direction
    current_position = complex(0,0)
    direction_facing = complex(0,1)
    # Run intcode for initial condition
    outputs = intcode(input_data, current_panel_colour, relative_base=relative_base)
    # Handling so we next update position
    full_instruction_received = False
    # If we haven't already painted it, it is black. Paint if it should be white.
    if (current_position not in white_panels) and (outputs[0] == 1):
        painted_panel_count += 1
        white_panels.append(current_position)
        if current_position not in painted_panels:
            distinct_painted_panel_count += 1
            painted_panels.append(current_position)
    elif (current_position in white_panels) and (outputs[0] == 0):
        painted_panel_count += 1
        white_panels.remove(current_position)
        if current_position not in painted_panels:
            distinct_painted_panel_count += 1
            painted_panels.append(current_position)

    while outputs[1] != 99:
        # First output value gives the colour to paint the panel
        if full_instruction_received and (outputs[1] != 99):
            outputs = intcode(outputs[4], current_panel_colour, outputs[2], outputs[3], outputs[0])
            if (current_position not in white_panels) and (outputs[0] == 1):
                painted_panel_count += 1
                white_panels.append(current_position)
                if current_position not in painted_panels:
                    distinct_painted_panel_count += 1
                    painted_panels.append(current_position)
            elif (current_position in white_panels) and (outputs[0] == 0):
                painted_panel_count += 1
                white_panels.remove(current_position)
                if current_position not in painted_panels:
                    distinct_painted_panel_count += 1
                    painted_panels.append(current_position)

            full_instruction_received = False
        if (not full_instruction_received) and (outputs[1] != 99):
            outputs = intcode(outputs[4], current_panel_colour, outputs[2], outputs[3], outputs[0])
            direction_to_turn = outputs[0]
            # Turning left 90 degress is like multiplying by i in the complex plain
            if direction_to_turn == 0:
                direction_facing = direction_facing*complex(0,1)
            # Turning right 90 degrees is like multiplying by -i in the complex plain
            if direction_to_turn == 1:
                direction_facing = direction_facing*complex(0,-1)
            current_position = current_position + direction_facing
            if current_position in white_panels:
                current_panel_colour = 1
            else:
                current_panel_colour = 0
            full_instruction_received = True
            # print("Now we are at " + str(current_position) + " which is colour " + str(current_panel_colour))
    return painted_panel_count, white_panels, distinct_painted_panel_count, painted_panels


# Part 1
# See what happens if we just run the input

NumberOfTimesPainted, WhitePanels, DistinctNumberPanelPainted, PanelsPainted = spaceship_painter(InputData)

# 2392 is the output (DistinctNumberPanelPainted)

# Part 2
# Start on a white panel
NumberOfTimesPainted2, WhitePanels2, DistinctNumberPanelPainted2, PanelsPainted2 = spaceship_painter(InputData, 1)

for x in range(len(WhitePanels2)):
        plt.plot([0,WhitePanels2[x].real],[0,WhitePanels2[x].imag],'ro', label='python')

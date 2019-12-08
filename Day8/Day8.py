# AoC 2019 Day 8

# Packages

import numpy as np

# Inputs

InputData = np.loadtxt("aoc2019_day8_input.txt",
                       dtype='str').tolist()

ImageWidth = 25
ImageHeight = 6

# Get a list of values

InputValues = []

for i in range(0,len(InputData)):
    InputValues.append(np.uint8(InputData[i]))

# Part 1

PixelsPerLayer = ImageWidth*ImageHeight
NumberOfLayers = int(len(InputValues)/PixelsPerLayer)

# Maximum number of zeros in a layer is the total number of pixels in a layer
CurrentLeastNumberOfZeros = PixelsPerLayer

for layer in range(0,NumberOfLayers):
    LayerStart = layer*PixelsPerLayer
    LayerEnd = LayerStart + PixelsPerLayer
    # print(LayerStart,LayerEnd)
    ThisLayer = InputValues[LayerStart:LayerEnd]
    ZeroValues = [value == 0 for value in ThisLayer]
    ZerosThisLayer = sum(ZeroValues)
    if ZerosThisLayer < CurrentLeastNumberOfZeros:
        CurrentLeastNumberOfZeros = ZerosThisLayer.copy()
        print("Current least number of zeros is " + str(CurrentLeastNumberOfZeros) + " in layer " + str(layer))
        OneValues = [value == 1 for value in ThisLayer]
        TwoValues = [value == 2 for value in ThisLayer]
        Result = sum(OneValues)*sum(TwoValues)

Result

# Part 2

# Decode the image
# Rules - keep ones and zeroes, defer two to the next layer

# Start with all twos - replace them as it makes sense
FinalImage = [2 for i in range(0,PixelsPerLayer)]

# Loop through layers, replacing 2 values in final image when appropriate
# Make use of nice Python True-False arithmetic (treat as 1 and 0)
for layer in range(0,NumberOfLayers):
    LayerStart = layer*PixelsPerLayer
    LayerEnd = LayerStart + PixelsPerLayer
    ThisLayer = InputValues[LayerStart:LayerEnd]
    TwosInFinalImage = [value == 2 for value in FinalImage]
    for k in range(0, len(FinalImage)):
        FinalImage[k] = (1-TwosInFinalImage[k])*FinalImage[k] + TwosInFinalImage[k]*ThisLayer[k]

FinalImageArray = np.array(FinalImage).reshape((ImageHeight,ImageWidth))
FinalImageArray
# Would be nice to write an image of this to the console to avoid having to use variable inspection
# One for further thought

# AoC 2019 Day 4

# Input

InputRange = "124075-580769"

# Part1
# Convert bounds to numbers
bounds = InputRange.split("-")
lowerBound = int(bounds[0])
upperBound = int(bounds[1])
# Define a list to collect valid passwords
validPasswords = []
# Loop through passwords checking criteria
# Don't need to worry about edge cases given they don't meet criteria
for password in range(lowerBound,upperBound):
    password = str(password)
    passwordList = [int(x) for x in password]
    # Check whether there are any cases where the password digits decrease
    allIncreasing = True
    for k in range(1,6):
        if passwordList[k] < passwordList[k-1]:
            allIncreasing = False
            break
    # Check if there are pairs of consecutive digits
    consecutiveDigits = False
    for k in range(1, 6):
        if passwordList[k] == passwordList[k - 1]:
            consecutiveDigits = True
    # Record a valid password only if conditions are met
    if allIncreasing & consecutiveDigits:
        validPasswords.append(password)

# Work out how many valid passwords there are
numberOfValidPasswords = len(validPasswords)

# Part 2
# Similar to part 1, but need to check there's at least one distinct pair of repeated digits, not just repeated digits
newValidPasswords = []
for password in range(lowerBound,upperBound):
    password = str(password)
    passwordList = [int(x) for x in password]
    # Check no decreasing digits
    allIncreasing = True
    for k in range(1,6):
        if passwordList[k] < passwordList[k-1]:
            allIncreasing = False
            break
    # Check for a distinct pair of consecutive digits
    consecutiveDigitsDistinctPair = False
    for k in range(1, 6):
        if passwordList[k] == passwordList[k - 1]:
            if (k == 1) and (passwordList[k + 1] != passwordList[k]):
                consecutiveDigitsDistinctPair = True
            elif (k == 5) and (passwordList[k - 2] != passwordList[k - 1]):
                consecutiveDigitsDistinctPair = True
            elif (k != 1) and (k != 5) and (passwordList[k + 1] != passwordList[k]) and \
                    (passwordList[k - 2] != passwordList[k - 1]):
                consecutiveDigitsDistinctPair = True
    # If both criteria are met, append to our list of valid passwords
    if allIncreasing & consecutiveDigitsDistinctPair:
        newValidPasswords.append(password)

# Calculate how many valid passwords there are now
numberOfNewValidPasswords = len(newValidPasswords)

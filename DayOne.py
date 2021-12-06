# Day 1 of Advent of Code

# Day 1 - Part 1
import csv

scanData = []

filename = 'AoCDay1Data.txt'

with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        scanData.append(row[0])
        for item in range(0, len(scanData)):
            scanData[item] = int(scanData[item])

    i = 0
    holding = 0
    increaseCounter = 0
    for i in range(0, len(scanData)):
        if scanData[i] < holding:
            holding = scanData[i]
        elif scanData[i] > holding:
            increaseCounter += 1
            holding = scanData[i]

print(scanData)
print('')
print("Day 1 - Part 1")
print(increaseCounter - 1, " Is the number of times the depth counter increased")


# Day 1 - Part 2 -------------------------------------------------------------------------------------------

def window_sliding_sum(data, a):
    n = len(data)
    if n < a:
        print("invalid")
        return -1

    slider_increase_counter = 0
    slider_hold = sum(data[:a])

    for k in range(n - a):

        # Removes the smallest index term in the sum and adds the next incoming term to update the slider
        slider = slider_hold - data[k] + data[k + a]

        # Compares the last window value with the current value to determine if there was an increase
        # in the current iteration.
        if slider > slider_hold:
            slider_increase_counter += 1

        # slider_holder holds that previous window sum so after every iteration it remembers the last
        # slider value.
        slider_hold = slider

    return slider_increase_counter


a = 3
print('')
print("Day 1 - Part 2")
print("Using the window sliding method of size 3, the data values increased: ", window_sliding_sum(scanData, a), "times.")

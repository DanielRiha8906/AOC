input = []
with open("Day_2/input.txt") as f:
    for line in f:
        line = line.strip().split(" ")
        placeholder = [int(element) for element in line]
        input.append(placeholder)


def is_increasing(input):
    for i in range(len(input) - 1):
        if input[i] > input[i + 1]:
            return False
    return True

def is_decreasing(input):
    for i in range(len(input) - 1):
        if input[i] < input[i + 1]:
            return False
    return True

def range_of_increase(input):
    for i in range(len(input) - 1):
        if abs(input[i] - input[i + 1]) < 1 or abs(input[i] - input[i + 1]) > 3:
            return False
    return True

counter = 0
for report in input:
    if (is_increasing(report) or is_decreasing(report)) and range_of_increase(report):
        counter += 1
    else:
        continue

print(counter)


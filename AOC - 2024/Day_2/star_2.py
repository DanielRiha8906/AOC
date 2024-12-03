input = []
with open("Day_2/input.txt") as f:
    for line in f:
        line = line.strip().split(" ")
        placeholder = [int(element) for element in line]
        input.append(placeholder)


def is_increasing(input):
    for i in range(len(input) - 1):
        if input[i] >= input[i + 1]:
            return False
    return True

def is_decreasing(input):
    for i in range(len(input) - 1):
        if input[i] <= input[i + 1]:
            return False
    return True

def range_of_increase(input):
    for i in range(len(input) - 1):
        if abs(input[i] - input[i + 1]) < 1 or abs(input[i] - input[i + 1]) > 3:
            return False
    return True

def validate(report):
    return ((is_increasing(report) or is_decreasing(report)) and range_of_increase(report))

def find_problematic_element(full_list):
    index = 0
    for element in full_list:
        temp_list = full_list.copy()
        temp_list.pop(index)
        index += 1
        if validate(temp_list):
            return element
    return None

counter = 0
for report in input:
    if validate(report):
        counter += 1
    else:
        if find_problematic_element(report) != None:
            counter += 1
        else:
            continue


print(counter)
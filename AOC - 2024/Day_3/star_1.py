import re
def read_file(file_path):
    with open(file_path, 'r') as file:
        file = file.read()
    return file

def regex(file):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    matches = re.findall(pattern, file)
    print(matches)

    pattern_two = r"\d{1,3}"
    matches_two = [re.findall(pattern_two, match) for match in matches]

    retyped_list = []
    for list_of_matches in matches_two:
        tmp_list = list(map(int, list_of_matches))
        retyped_list.append(tmp_list)
    result = 0
    for semi_lists in retyped_list:
        result = result + semi_lists[0] * semi_lists[1]
    return result

def main():
    input = read_file("Day_3/input.txt")
    pairs = regex(input)
    print(pairs)

if __name__ == "__main__":
    main()
def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        column_one = []
        column_two = []


        for line in lines:
            line = line.strip()
            
            if not line: 
                continue
            
            parts = line.split()
            
            if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                print(f"Invalid line skipped: {line}")
                continue


            column_one.append(int(parts[0]))
            column_two.append(int(parts[1]))
        
        return column_one, column_two
    
    except FileNotFoundError:
        #print(f"Error: The file '{file_path}' was not found.")
        return [], []


def main():

    input_file = "Day1/input.txt"

    column_one, column_two = process_file(input_file)
    result = 0
    sorted_column_one = sorted(column_one)
    sorted_column_two = sorted(column_two)
    for i in range(len(sorted_column_one)):
        result = result + (abs(sorted_column_one[i] - sorted_column_two[i]))
        
    print(result)
if __name__ == "__main__":
    main()

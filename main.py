from solution import increasing_to_decreasing

def read_arrays_from_file(file_path):
    with open(file_path, 'r') as file:
        arrays = []
        for line in file:
            array = list(map(int, line.strip().split(',')))
            arrays.append(array)
    return arrays

def main():
    arr = read_arrays_from_file("test.txt")
    
    for i in range(len(arr)):
        change_point = increasing_to_decreasing(arr[i])
        print(f"The change point index of the {i+1} array is: {change_point}")

if __name__ == "__main__":
    main()
    
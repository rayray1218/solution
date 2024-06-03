def increasing_to_decreasing(arr):
    if len(arr) <= 2:
        return -1
    else:
        if arr[0] < arr[1]:
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return i
            return -1
        elif arr[0] > arr[1]:
            for i in range(len(arr) - 1):
                if arr[i] < arr[i+1]:
                    return i
            return -1
        else:
            return -1
def binary_search(array, value):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if(array[mid] == value):
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1

test = [1,2,3,4,5,6,7,8,9]
print("Element found at position : ", binary_search(test, 9))
            

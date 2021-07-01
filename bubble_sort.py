def bs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            else :
                pass
    return array

array = [11,1,12,34,7,8,56,4,0]
print("Sorted array : ", bs(array), sep = ' ', end = '')

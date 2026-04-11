# Selection Sort

def SelectionSort(array, size):
    x = 1
    for indx in range(size):
        min_index = indx

        for j in range(indx + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        
        array[indx], array[min_index] = array[min_index], array[indx]
        print("PASS ", x, "=", arr)
        x += 1

arr = [-2, 45, 32, -34, 50, 164, -100, 2034, -3422, 345]
size = len(arr)
SelectionSort(arr, size)
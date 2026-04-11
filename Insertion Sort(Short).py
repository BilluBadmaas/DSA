# Insertion Sort

def InsertionSort(arr):
    x = 1
    n = len(arr)

    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
        print("Pass", x, "=", arr)
        x += 1

arr = [12,934,40,324,10,3]
InsertionSort(arr)
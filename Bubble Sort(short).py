# Bubble Sort

def BubbleSort(arr):
    x = 1
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Pass", x, "=", arr)
                x += 1

                swapped = True

        if not swapped:
            break

arr = [233, 423, 94, 67, 342, 34]
BubbleSort(arr)
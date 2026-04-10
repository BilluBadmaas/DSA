def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #

# Get user array
data = input("Enter numbers separated by space: ").split()
arr = [int(x) for x in data]

print("Choose Sort: 1. Bubble  2. Selection")
choice = input("Choice: ")
if choice == '1': bubbleSort(arr)
else: selectionSort(arr)

print("Sorted Array:", arr)

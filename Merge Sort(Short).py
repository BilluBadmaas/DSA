# Merge Sort

x = 1
def MergeSort(arr):
    global x
    n = len(arr)

    if n > 1:
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print("Pass ", x, "=", arr)
        x += 1

arr = [12,234,356,567,2143246,457,14]
MergeSort(arr)
def countingSort(arr):
    a = [0 for i in range(100)]
    for i in arr:
        a[i] += 1
    return a

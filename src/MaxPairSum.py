def maxPair(arr):
    if len(arr) < 2:
        raise ValueError("Input array must contain at least two elements")

    max_sum = float('-inf')
    max_indices = (0, 1)

    for i in range(len(arr) - 1):
        curr_sum = arr[i] + arr[i + 1]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_indices = (i, i + 1)

    return max_indices
arr = [0, 5, 5, 2]
indices = maxPair(arr)
print(indices) 
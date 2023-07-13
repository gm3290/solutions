def pairs(k, arr):
    my_dict = {}
    result = 0
    for ele in arr:
        my_dict[ele] = 1
        if ele + k in my_dict:
            result += 1
        if ele - k in my_dict:
            result += 1
    return result


k = 2
arr = [1, 5, 3, 4, 2]

print(pairs(k, arr))

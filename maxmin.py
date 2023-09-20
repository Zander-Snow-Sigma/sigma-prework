def maxmin(arr):
    min = arr[0]
    max = arr[0]
    for num in arr:
        if num < min:
            min = num
        if num > max:
            max = num
    return [min, max]


print(maxmin([2, 4, 1, 0, 2, -1]))

def maxmin(number_array):
    if len(number_array) <= 0:
        print("Invalid input")
        return

    max = number_array[0]
    min = max

    for i in number_array:
        if i > max:
            max = i
        if i < min:
            min = i
    
    return [min, max]


# print(maxmin([2, 4, 1, 0, 2, -1]))
# print(maxmin([10, 50, 12, 6, 14, 8]))
# print(maxmin([100, -100]))
#Complete the function that
#     accepts two integer arrays of equal length
#   compares the value each member in one array to the corresponding member in the other
#   squares the absolute value difference between those two values
#   and returns the average of those squared absolute value difference between each member pair.


def solution(array_a, array_b):
    added_numbers = 0
    for i in range(len(array_a)):
        added_numbers += (abs(array_a[i] - array_b[i]) * abs(array_a[i] - array_b[i]))
    return added_numbers / len(array_b)
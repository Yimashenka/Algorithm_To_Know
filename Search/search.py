"""

"""


# LINEAR SEARCH
def linear_search(array, N, value):
    """
    :param array: The array to search in
    :param N: The range of the array (generally len(array))
    :param value: The value to find
    :return: The first position where the value is found, or -1 if not present
    """
    result = -1
    for i in range(0, N):
        if array[i] == value and result == -1:
            result = i

    return result


def linear_search_v2(array, value):
    """
    Another version
    :param array: the array to search in
    :param value: the value to find in the array
    :return: The first position where the value is found, or -1 if not present
    """
    try:
        result = array.index(value)
    except ValueError:
        result = -1

    return result


# BINARY SEARCH
def binary_search(array, value):
    """
    :param array: The array to search in
    :param value: The value to find
    :return: The position of the value in the array, -1 if not in
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = left + (right - 1) // 2

        if array[middle] ==  value:
            return middle
        elif array[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    return -1


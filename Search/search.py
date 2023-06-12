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
def binary_search(array, value, l, r):
    """
    :param array: The array to search in
    :param value: The value to find
    :return: The position of the value in the array, -1 if not in
    """

    while l <= r:
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if array[mid] == value:
            return mid

        # If x is greater, ignore left half
        elif array[mid] < value:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


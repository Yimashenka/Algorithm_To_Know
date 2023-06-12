"""

"""


# BUBBLE SORT
def bubble_sort(array):
    """
    :param array: the array to sort
    :return: nothing, modify the array put as parameter
    """

    n = len(array)

    # We will iterate through all the elements
    for i in range(0, n):
        swapped = False

        # The last i elements are in place
        for j in (0, n - i - 1):

            # We swapped if the element is greater than the next one
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if swapped:
            break


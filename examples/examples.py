from Search.search import *

# DATA
not_sorted_array = [-12, 15, 156, 8, -17, -6, 2, 1, 59, -85]
sorted_array = [-10, -8 ,-7, -6, 0, 21, 56, 89, 115]

# SEARCH
# Linear Search
print(linear_search(not_sorted_array, len(not_sorted_array), 2))
print(linear_search_v2(not_sorted_array, 0))

# Binary Search
print(binary_search(sorted_array, 21, 0, len(sorted_array)))
print(binary_search(sorted_array, 100, 0, len(sorted_array)))


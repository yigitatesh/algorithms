## Linear search
def linear_search(key, array):
    """Linear search implementation

    Parameters
    ----------
    key: key to search in array
    array: a sorted array"""
    for i, n in enumerate(array):
        if n == key:
            return i
    return -1

def linear_search2(key, array):
    """Linear search implementation without enumerate function"""
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

## Binary Search
def binary_search(key, array):
    """Binary search
    
    Parameters
    ----------
    key: key to search in array
    array: a sorted array"""
    low = -1
    high = len(array)
    while high - low > 1:
        mid = (high + low) // 2
        
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid
        else: # array[mid] > key
            high = mid
    return -1
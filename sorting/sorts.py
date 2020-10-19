## BUBBLE SORT
def bubble_sort_non_optimised(array):
    """Bubble sort implementation"""
    new_array = array.copy()
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(new_array) - 1):
            if new_array[i] > new_array[i+1]:
                new_array[i], new_array[i+1] = new_array[i+1], new_array[i]
                is_sorted = False
    
    return new_array

def bubble_sort(array):
    """Bubble sort implementation
    Optimised:
        for each iteration, length of unsorted array decreases 1"""
    new_array = array.copy()
    is_sorted = False
    last_unsorted = len(new_array) - 1
    
    while not is_sorted:
        is_sorted = True
        for i in range(0, last_unsorted):
            if new_array[i] > new_array[i+1]:
                new_array[i], new_array[i+1] = new_array[i+1], new_array[i]
                is_sorted = False
        last_unsorted -= 1
    
    return new_array

## INSERTION SORT
def insertion_sort(array):
    """Insertion sort implementation"""
    new_array = array.copy()

    for i in range(1, len(new_array)):
        j = i
        while j > 0 and new_array[j-1] > new_array[j]:
            new_array[j-1], new_array[j] = new_array[j], new_array[j-1]
            j -= 1
    
    return new_array

## SELECTION SORT
def selection_sort(array):
    """Selection sort implementation"""
    new_array = array.copy()
    
    for i in range(len(new_array)):
        j = i
        min_num = j
        while j < len(new_array):
            if new_array[j] < new_array[min_num]:
                min_num = j
            j += 1
        new_array[i], new_array[min_num] = new_array[min_num], new_array[i]
    d
    return new_array      

## MERGE SORT
def merge_sort(array):
    """Merge sort implementation"""
    if len(array) > 1:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)
    else:
        return array

def merge(left, right):
    """Merge function of merge sort"""
    sorted_list = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    while len(left) > 0:
        sorted_list.append(left.pop(0))
    while len(right) > 0:
        sorted_list.append(right.pop(0))
        
    return sorted_list

## QUICK SORT
def quick_sort(array):
    """Quick sort in place"""
    return _quick_sort(array, 0, len(array) - 1)

def _quick_sort(array, left, right):
    
    if left >= right:
        return None
    # pick a pivot
    pivot = array[left + (right - left) // 2]
    index = partition(array, left, right, pivot)
    _quick_sort(array, left, index - 1)
    _quick_sort(array, index, right)

def partition(array, left, right, pivot):
    """sorts array by looking to pivot"""
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        
        if left <= right:
            # swap two numbers
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
            
    return left

## QUICK SORT PYTHONIC
def quick_sort_simple(array):
    """Quick sort that easy to understand"""
    if len(array) < 2:
        return array
    # choose pivot
    pivot = array.pop()
    left = []
    right = []
    
    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    return quick_sort_simple(left) + [pivot] + quick_sort_simple(right)

## COUNT SORT
def count_sort(array, low, high):
    """Count sort
    Every element must be integer
    
    Parameters
    ----------
    array: array or list to be sorted in place
    low: min integer in array
    high: max integer in array"""
    # hash map of integers and frequencies
    hash_map = {i: 0 for i in range(low, high + 1)}
    for i in array:
        hash_map[i] += 1
    
    # create new sorted array
    length = len(array)
    i = 0
    for j in range(low, high + 1):
        for _ in range(hash_map[j]):
            array[i] = j
            i += 1
    
    return array

## STOOGE SORT
def stooge_sort(array):
    """Stooge sort
    Changes the list in place"""
    _stooge_sort(array, 0, len(array)-1)

def _stooge_sort(array, low, high):
    if array[low] > array[high]:
        array[low], array[high] = array[high], array[low]
    if high - low <= 1:
        return None
    
    dif = (high - low + 1) // 3
    
    _stooge_sort(array, low, high - dif)
    _stooge_sort(array, low + dif, high)
    _stooge_sort(array, low, high - dif)

## BOGO SORT
def bogo_sort(array):
    """Bogo sort"""
    new_array = array.copy()
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        np.random.shuffle(new_array)
        for i in range(len(new_array) - 1):
            if new_array[i] > new_array[i+1]:
                is_sorted = False
                break
    return new_array
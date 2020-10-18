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
import numpy as np

## Fisher-Yates
def shuffle_old(array):
    """Old Fisher-Yates shuffle"""
    new_array = array.copy()
    shuffled = []
    while len(new_array) > 0:
        rand_index = np.random.randint(0, len(new_array))
        shuffled.append(new_array[rand_index])
        new_array.pop(rand_index)
    return shuffled

def shuffle(array):
    """Optimised Fisher-Yates shuffle"""
    new_array = array.copy()
    last_index = len(new_array) - 1
    while last_index > 0:
        rand_index = np.random.randint(0, last_index)
        new_array[last_index], new_array[rand_index] = new_array[rand_index], new_array[last_index]
        last_index -= 1
    return new_array

## Random Indexes Shuffle
def shuffle_rand_indexes(array):
    """shuffle with making a random number list and sorting it"""
    new_array = array.copy()
    rand_values = [np.random.rand() for i in range(len(array))]
    rand_indexes = list(range(len(new_array)))
    rand_indexes.sort(key=lambda x: rand_values[x])
    new_array = [new_array[i] for i in rand_indexes]
    return new_array
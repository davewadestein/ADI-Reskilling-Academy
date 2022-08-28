def slicer(iterable, pos1, length):
    """Return a slice from pos1 to pos1 + length, but also handle wraparound, so 
    if pos1 + length goes past the end of the iterable, start back at the beginning
    """
    if pos1 + length <= len(iterable):
        return iterable[pos1:pos1 + length]
    else:
        part1 = iterable[pos1:]
        return part1 + iterable[:length - len(part1)]

    
def find3(iterable):
    """Identify all "runs" of 3 of the same object in a container and
    return a list of their initial index. Here are some examples:
    
        find3(['one', 'two', 'three', 'four', 'four', 'four', 'five', 'six']) == [3]
        find3([1, 2, 2, 2, 2, 3]) == [1, 2]
        find3([48, 47, 47, 47, 19, 23, 14, 14, 14, 18, 48]) == [1, 6]
        find3([48, 48, 'forty eight', 'forty eight', 'forty eight', 38, 39, -1, 2]) == [2]
        find3([1, 2, 3, 2, 2]) == []
        
    Runs can "wrap around" the end of the container, so, for e.g.,
    
        find3([1, 2, 5, -4, 3, 1, 1]) == [5]
    """
    # Compare each consecutive group of 3 items for equality and note any that are found
    # NOTE: since our goal is to find identical items, we could set-ify each group of 3,
    # looking for a resulting set size of 1.
    # Or, we could compare [i] to [i + 1] and to [i + 2]
    
    # We're going to return a list of runs, which should start out empty.
    runs = []
    
    # Now we will "walk" through the iterable/container one element at a time and
    # generate a slice of 3 items. We'll use the slicer() function in order to 
    # allow wraparound from end to beginnging. If no wraparound was needed, we
    # could use standard Python slicing.
    
    for index in range(len(iterable)):
        print('examining', slicer(iterable, index, 3))
        
        # Each "slice" of 3 items must be checked to see if all 3 items are the same.
        # We could check if [0] == [1] and [0] == [2], or we could do it easier by
        # dropping all 3 into a set and seeing how many are in the set. If all the
        if len(set(slicer(iterable, index, 3))) == 1: 
            runs.append(index)
    return runs
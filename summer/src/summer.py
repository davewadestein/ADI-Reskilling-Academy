def summer(container, total):
    """Search container for a slice of consecutive values whose total
    is total.
    """
    
    # algorithm
    # start at beginning of list
    # "grow a slice" until sum is >= desired sum
    # if =, then return that slice
    # if >, the move forward to next index
    start = 0
    
    while start <= len(container):
        end = start + 1
        while end <= len(container):
            print('summing', container[start:end])
            if sum(container[start:end]) == total:
                return container[start:end]
            end += 1
        start += 1
        
    return []
# let's write some tests

from find3 import find3, slicer

# any function that beging with "test_" will be "discovered" by pytest and run

def test_empty():
    assert find3([]) == []
    
    
def test_strings():
    assert find3(['one', 'two', 'three', 'four', 'four', 'four', 'five', 'six']) == [3]


def test_overlap():
    assert find3([1, 2, 2, 2, 2, 3]) == [1, 2]
    

def test_no_overlap():
    assert find3([48, 47, 47, 47, 19, 23, 14, 14, 14, 18, 48]) == [1, 6]
    

def test_mixed():
    assert find3([48, 48, 'forty eight', 'forty eight', 'forty eight', 38, 39, -1, 2]) == [2]
    
    
def test_no_runs():
    assert find3([1, 2, 3, 2, 2]) == []
    
    
def test_wrap():
    assert find3([1, 2, 5, -4, 3, 1, 1]) == [5]
    

# in order to implement the wraparound behavior, whereby a run can start at last or second to last 
# element in the container and "wrap around" back to the beginning, I created a function called slicer
# which returns a slice of the list, with wraparound if necessary. So it's important that I test that
# function as well.

def test_slicer_empty():
    assert slicer([], 4, 3) == []
    

def test_slicer_no_wrap():
    assert slicer([0, 1, 2, 3, 4, 5], 2, 3) == [2, 3, 4]
    
    
def test_slicer_wrap1():
    assert slicer([0, 1, 2, 3, 4], 3, 3) == [3, 4, 0]

    
def test_slicer_wrap2():
    assert slicer([0, 1, 2, 3, 4], 4, 3) == [4, 0, 1]
    

def test_slicer_short_container():
    assert slicer([0], 0, 3) == []
    
    
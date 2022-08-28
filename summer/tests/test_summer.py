from ..src.summer import summer

def test_empty():
    assert summer([], 1) == []
    
    
def test_all():
    assert summer([1, 2, 3, 4, 5], 15) == [1, 2, 3, 4, 5]
    
    
def test_some():
    assert summer([1, 2, 3, 4, 5, 6, 7, 8], 26) == [5, 6, 7, 8]
    

def test_none():
    assert summer([1, 2, 3, 4, 5, 6, 7, 8], 19) == []
    

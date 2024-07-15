import pytest
from BubbleSort import bubblesort

def test_bubblesort():
    # Test case 1: Regular list
    assert bubblesort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]
    
    # Test case 2: Already sorted list
    assert bubblesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 3: List sorted in reverse
    assert bubblesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Test case 4: List with duplicates
    assert bubblesort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]
    
    # Test case 5: List with one element
    assert bubblesort([1]) == [1]
    
    # Test case 6: Empty list
    assert bubblesort([]) == []
    
    # Test case 7: List with negative numbers
    assert bubblesort([3, -1, -4, 2, 0]) == [-4, -1, 0, 2, 3]

if __name__ == "__main__":
    pytest.main()


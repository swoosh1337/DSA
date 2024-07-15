import pytest
from BinarySearchList import binarysearchlist

def test_binarysearchlist():
    # Test case 1: Search for an existing element in the middle
    assert binarysearchlist([1, 3, 5, 7, 9], 5) == True

    # Test case 2: Search for a non-existing element
    assert binarysearchlist([1, 3, 5, 7, 9], 4) == False

    # Test case 3: Search in an empty list
    assert binarysearchlist([], 1) == False

    # Test case 4: Search for the first element
    assert binarysearchlist([1, 3, 5, 7, 9], 1) == True

    # Test case 5: Search for the last element
    assert binarysearchlist([1, 3, 5, 7, 9], 9) == True

    # Test case 6: Search in a list with one element (True case)
    assert binarysearchlist([1], 1) == True

    # Test case 7: Search in a list with one element (False case)
    assert binarysearchlist([1], 2) == False

    # Test case 8: Search for a negative number
    assert binarysearchlist([-9, -3, 0, 5, 12], -3) == True

    # Test case 9: Test with large sorted list
    large_list = list(range(0, 10000, 2))  # Even numbers from 0 to 9998
    assert binarysearchlist(large_list, 5000) == True
    assert binarysearchlist(large_list, 5001) == False

    # Test case 10: Test with duplicate elements
    assert binarysearchlist([1, 2, 2, 2, 3, 4, 5], 2) == True

    # Test case 11: Test edge cases (just outside the range)
    assert binarysearchlist([1, 3, 5, 7, 9], 0) == False
    assert binarysearchlist([1, 3, 5, 7, 9], 10) == False

    # Test case 12: Test with floating point numbers
    assert binarysearchlist([1.1, 2.2, 3.3, 4.4, 5.5], 3.3) == True
    assert binarysearchlist([1.1, 2.2, 3.3, 4.4, 5.5], 3.2) == False

if __name__ == "__main__":
    pytest.main()

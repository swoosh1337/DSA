import pytest
from LinearSearchList import linearsearchlist

def test_linearsearchlist():
    # Test case 1: Search for an existing element
    assert linearsearchlist([1, 3, 5, 7, 9], 5) == True

    # Test case 2: Search for a non-existing element
    assert linearsearchlist([1, 3, 5, 7, 9], 4) == False

    # Test case 3: Search in an empty list
    assert linearsearchlist([], 1) == False

    # Test case 4: Search for the first element
    assert linearsearchlist([1, 3, 5, 7, 9], 1) == True

    # Test case 5: Search for the last element
    assert linearsearchlist([1, 3, 5, 7, 9], 9) == True

    # Test case 6: Search in a list with one element (True case)
    assert linearsearchlist([1], 1) == True

    # Test case 7: Search in a list with one element (False case)
    assert linearsearchlist([1], 2) == False

    # Test case 8: Search for a negative number
    assert linearsearchlist([-3, -1, 0, 1, 3], -1) == True

    # Test case 9: Test with duplicate elements
    assert linearsearchlist([1, 2, 2, 3, 4, 2], 2) == True

    # Test case 10: Test with all same elements
    assert linearsearchlist([5, 5, 5, 5, 5], 5) == True

if __name__ == "__main__":
    pytest.main()

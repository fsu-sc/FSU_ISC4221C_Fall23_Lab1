# Unit test for a sorting algorithm
import pytest
from answers_lab import selection_sort

def test_selection_sort():
    # Test with a list of integers
    lst = [5, 3, 8, 1, 2, 7, 4, 6]
    sorted_lst = selection_sort(lst)
    assert sorted_lst == [1, 2, 3, 4, 5, 6, 7, 8]

    # Test with an empty list
    lst = []
    sorted_lst = selection_sort(lst)
    assert sorted_lst == []

    # Test with a list of one element
    lst = [5]
    sorted_lst = selection_sort(lst)
    assert sorted_lst == [5]

    # Test with a list of repeated elements
    lst = [3, 3, 3, 3, 3]
    sorted_lst = selection_sort(lst)
    assert sorted_lst == [3, 3, 3, 3, 3]
import pytest
from brute_force import two_sum_brute_force
from optimized_solution import two_sum_hash_table

@pytest.mark.parametrize("func, nums, target, expected", [
    (two_sum_brute_force, [2, 7, 11, 15], 9, [0, 1]),
    (two_sum_hash_table, [2, 7, 11, 15], 9, [0, 1]),
    (two_sum_brute_force, [3, 2], 7, None),
    (two_sum_hash_table, [3, 2], 7, None)
])
def test_two_sum_methods(func, nums, target, expected):
    assert func(nums, target) == expected

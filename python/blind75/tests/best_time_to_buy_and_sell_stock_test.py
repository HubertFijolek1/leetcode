import pytest
import time
from ..best_time_to_buy_and_sell_stock.brute_force import max_profit_brute_force
from ..best_time_to_buy_and_sell_stock.one_pass_solution import max_profit_one_pass

@pytest.mark.parametrize("func, prices, expected", [
    # General Cases
    (max_profit_brute_force, [2, 7, 11, 15], 13),
    (max_profit_one_pass, [2, 7, 11, 15], 13),
    (max_profit_brute_force, [3, 2], 0),
    (max_profit_one_pass, [3, 2], 0),
    (max_profit_brute_force, [7, 1, 5, 3, 6, 4], 5),
    (max_profit_one_pass, [7, 1, 5, 3, 6, 4], 5),
    (max_profit_brute_force, [7, 6, 4, 3, 1], 0),
    (max_profit_one_pass, [7, 6, 4, 3, 1], 0),

    # Edge Cases
    (max_profit_brute_force, [], 0),
    (max_profit_one_pass, [], 0),
    (max_profit_brute_force, [1], 0),
    (max_profit_one_pass, [1], 0),
    (max_profit_brute_force, [7, 7, 7, 7, 7], 0),
    (max_profit_one_pass, [7, 7, 7, 7, 7], 0),

    # Large Inputs
    (max_profit_brute_force, [i for i in range(100)], 99),  # Increasing sequence
    (max_profit_one_pass, [i for i in range(100)], 99),
    (max_profit_brute_force, [100 - i for i in range(100)], 0),  # Decreasing sequence
    (max_profit_one_pass, [100 - i for i in range(100)], 0),
    (max_profit_brute_force, [1]*20000, 0),  # All identical elements
    (max_profit_one_pass, [1]*20000, 0),
])
def test_max_profit_methods(func, prices, expected):
    start_time = time.time()
    assert func(prices) == expected
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution time for {func.__name__} with input {prices[:10]}...: {duration:.6f} seconds")

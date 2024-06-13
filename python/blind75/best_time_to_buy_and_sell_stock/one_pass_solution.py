"""
This solution maintains two variables: `min_price` and `max_profit`.

- Iterates through the prices list once.
- Updates `min_price` to keep track of the lowest price seen so far.
- Updates `max_profit` to track the maximum profit achievable by selling on the current day.
- This approach has a time complexity of O(n).

"""
def max_profit_one_pass(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Example usage:
# prices = [7, 1, 5, 3, 6, 4]
# print(max_profit_one_pass(prices))  # Output: 5

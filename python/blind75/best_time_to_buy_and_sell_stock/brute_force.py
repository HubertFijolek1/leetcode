'''
In this solution, we compare every possible pair of buying and selling days to find the maximum profit. This approach has a time complexity of O(n2).
'''

def max_profit_brute_force(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

# Example usage:
# prices = [7, 1, 5, 3, 6, 4]
# print(max_profit_brute_force(prices))  # Output: 5
        



def max_profit_brute_force(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

# prices = [7, 1, 5, 3, 6, 4]
# print(max_profit_brute_force(prices))  # Output: 5
        



def maxProfit(prices):
    buy_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]
        else:
            current_profit = prices[i] - buy_price
            max_profit = max(current_profit, max_profit)
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit([3, 2, 1, 4]))

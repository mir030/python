def maxProfit(prices):
    max_profit = 0
    buy = prices[0]
    for price in prices:
        if buy > price:
            buy = price
        else:
            max_profit = max(max_profit, price - buy)
    return max_profit

print(maxProfit([7, 6, 5, 3, 2, 1]))
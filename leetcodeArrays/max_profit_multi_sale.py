
# Since you can buy it on the same day, the idea is to always update buy price after selling
def maxProfit(prices):
    buy_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]
        else:
            profit += prices[i] - buy_price
            buy_price = prices[i]
    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

prices_2 = [1, 2, 3, 4, 5]
print(maxProfit(prices_2))
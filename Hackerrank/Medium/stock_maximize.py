def max_profit(prices):
    max_sell_price = prices[-1]
    profit = 0
    for price in prices[len(prices) - 2:: -1]:
        if price < max_sell_price:
            temp = max_sell_price - price
            if temp > profit:
                profit = temp
        else:
            max_sell_price = price
    return profit


prices = [5, 1]
print(max_profit(prices))


def stocks_max(prices):
    profits = 0
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > profits:
                profits = profit

    return profits


print(stocks_max(prices))

print(sum(bytearray("Mir Karim", encoding='utf-8')))
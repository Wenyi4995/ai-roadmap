"""买卖股票的最佳时机：一次遍历求最大利润。"""


def max_profit(prices):
    if not prices:
        return 0

    lowest_price = prices[0]
    best_profit = 0

    for price in prices:
        if price < lowest_price:
            lowest_price = price
        else:
            current_profit = price - lowest_price

            if current_profit > best_profit:
                best_profit = current_profit

    return best_profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
assert max_profit([2, 4, 1]) == 2

print("所有测试通过")

denominations_asc = [1, 2, 5, 10, 25, 50]
denominations_desc = sorted(denominations_asc, reverse=True)

def find_coins_greedy(amount):
    change = {}

    for coin in denominations_desc:
        count = amount // coin
        if count > 0:
            change[coin] = count
            amount -= count * coin

    return change

def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    used_coins = [0] * (amount + 1)

    for coin in denominations_asc:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = coin

    coins_used = {}
    while amount > 0:
        coin = used_coins[amount]
        if coin in coins_used:
            coins_used[coin] += 1
        else:
            coins_used[coin] = 1
        amount -= coin

    return coins_used

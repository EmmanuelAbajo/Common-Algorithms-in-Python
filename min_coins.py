''' Dynamic programming has two approaches
1. Top down approach (Memorization): This is usually recursive
2. Bottom top approach (Tabulation): This is usually iterative
This paradigm excels for optimization or permutation problems (in how many ways problems) '''
def find_min_coins(coins, target):
    if target == 0:
        return 0
    table = [float('inf')] * (target+1)
    table[0] = 0
    for coin in coins:
        for i in range(coin, target+1):
            subproblem = i - coin
            table[i] = min(table[i], table[subproblem] + 1)
    
    return table[target] if table[target] != float('inf') else -1

def find_minimum_coins(coins, target):
    if target < 0:
        return 0
    table = [float('inf')] * (target+1)
    table[0] = 0
    for i in range(1, target+1):
        for coin in coins:
            if i-coin >= 0:
                table[i] = min(table[i], 1+table[i-coin])
    
    return table[target] if table[target] != float('inf') else -1





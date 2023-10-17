def get_coin_change_ways(coins, target: int) -> int:
    if target == 0:
        return 1
    table = [0] * (target+1) 
    table[0] = 1
    for i in range(1, target+1):
        for coin in coins:
            if i - coin >= 0: # means you can use this coin
                table[i]+=table[i-coin]
    return table[target]     

def get_coin_change_ways_unique(coins, target: int,) -> int:
        n = len(coins)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Fill 1st row with 0 because no target (except 0) can be formed without any coin
        for i in range(1, target + 1):
            dp[0][i] = 0

        # Fill 1st col by 1 (assuming target 0 can always be formed)
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill DP-Table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]   
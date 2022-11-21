def knapsack01(wt:list(), val: list(), W, n):
    # dp = [[0 for x in range(cols)] for x in range(rows)]
    dp = [[0 for x in range(W + 1)] for x in range(n+1)]
    
    for i in range(n + 1):
        for j in range(W + 1): # i => n and j => W
            
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            
            # included cur weight
            if wt[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i-1])
                continue
            
            # excluded cur weight
            dp[i][j] = dp[i - 1][j]
            
    return dp[n][W]

if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    print(knapsack01(wt, val, W, 3))
    
    
    
    
    




            
        
            
    
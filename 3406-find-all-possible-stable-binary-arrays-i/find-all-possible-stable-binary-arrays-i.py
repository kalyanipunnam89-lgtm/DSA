class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        for i in range(1, min(limit, zero) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero+1):
            for j in range(1, one+1):
                x = 0 if i-limit-1 < 0 else dp[i-limit-1][j][1]
                y = 0 if j-limit-1 < 0 else dp[i][j-limit-1][0]
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1] - x) % MOD
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1] - y) % MOD
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
        
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * 101 for _ in range(101)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    extra = dp[i][j] - 1
                    dp[i][j] = 1
                    dp[i+1][j] += extra / 2
                    dp[i+1][j+1] += extra / 2
        return min(1.0,dp[query_row][query_glass])
        
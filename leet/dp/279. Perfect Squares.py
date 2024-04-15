class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i**2 for i in range(1, 101)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for ps in perfect_squares:
            for x in range(ps, n+1):
                dp[x] = min(dp[x], dp[x-ps] + 1)
        return dp[n] if dp[n] != float('inf') else -1

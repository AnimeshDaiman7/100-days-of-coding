class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = 1

        for nodes in range(1, n + 1):
            for root in range(nodes):
                dp[nodes] += dp[root] * dp[nodes - root - 1]

        return dp[n]

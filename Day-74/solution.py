class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        # pal[i][j] tells whether s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                if s[i] == s[j] and (
                    j - i <= 2 or pal[i + 1][j - 1]
                ):
                    pal[i][j] = True

        # cuts[i] = minimum cuts needed for s[0:i+1]
        cuts = [0] * n

        for i in range(n):

            if pal[0][i]:
                cuts[i] = 0
            else:
                cuts[i] = i

                for j in range(1, i + 1):

                    if pal[j][i]:
                        cuts[i] = min(
                            cuts[i],
                            cuts[j - 1] + 1
                        )

        return cuts[n - 1]

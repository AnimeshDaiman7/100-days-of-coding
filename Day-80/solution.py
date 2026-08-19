class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def solve(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern completely processed
            if j == len(p):
                return i == len(s)

            # String completely processed
            if i == len(s):
                result = all(ch == '*' for ch in p[j:])
                memo[(i, j)] = result
                return result

            # Current characters match
            if p[j] == s[i] or p[j] == '?':
                result = solve(i + 1, j + 1)

            # '*' can match zero or more characters
            elif p[j] == '*':
                result = (
                    solve(i, j + 1) or
                    solve(i + 1, j)
                )

            else:
                result = False

            memo[(i, j)] = result
            return result

        return solve(0, 0)

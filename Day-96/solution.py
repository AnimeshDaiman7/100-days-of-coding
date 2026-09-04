from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dy = y2 - y1
                dx = x2 - x1

                g = gcd(dy, dx)

                dy //= g
                dx //= g

                if dx < 0:
                    dy = -dy
                    dx = -dx

                slopes[(dy, dx)] += 1

                ans = max(ans, slopes[(dy, dx)] + 1)

        return ans

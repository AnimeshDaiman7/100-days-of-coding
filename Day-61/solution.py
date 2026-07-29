from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        countT = Counter(t)
        window = {}

        have = 0
        need = len(countT)

        left = 0
        result = [-1, -1]
        resultLen = float("inf")

        for right in range(len(s)):

            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:

                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1

                window[s[left]] -= 1

                if (
                    s[left] in countT and
                    window[s[left]] < countT[s[left]]
                ):
                    have -= 1

                left += 1

        left, right = result

        return s[left:right + 1] if resultLen != float("inf") else ""

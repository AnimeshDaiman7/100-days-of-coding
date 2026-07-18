class Solution:
    def numDecodings(self, s: str) -> int:

        one = 1
        two = 0

        for i in range(len(s) - 1, -1, -1):

            curr = 0

            if s[i] != "0":
                curr = one

                if (
                    i + 1 < len(s)
                    and (
                        s[i] == "1"
                        or (s[i] == "2" and s[i + 1] <= "6")
                    )
                ):
                    curr += two if i + 2 < len(s) else 1

            two = one
            one = curr

        return one

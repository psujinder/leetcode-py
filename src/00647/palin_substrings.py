class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPalin(s: str, lo: int, hi: int) -> int:
            count = 0

            while lo >= 0 and hi < len(s):
                if s[lo] != s[hi]:
                    return count

                lo -= 1
                hi += 1
                count += 1

            return count

        ans = 0

        for idx in range(0, len(s)):

            ans += checkPalin(s, idx, idx)
            ans += checkPalin(s, idx, idx + 1)

        return ans

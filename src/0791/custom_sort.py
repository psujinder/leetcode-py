class Solution:
    def customSortString(self, order: str, s: str) -> str:

        s_map = {}
        result = ""

        for ch in s:
            if ch in s_map:
                s_map[ch] += 1
            else:
                s_map[ch] = 1

        for ch in c:
            if ch in s_map:
                result += ch * s_map[ch]
                s_map.pop(ch)

        for key, val in s_map.items():
            result += key * val

        return result


class Solution:
    def maximumSwap(self, num: int) -> int:
        
        s = list(str(num))
        arr = [0]* len(s)

        arr[-1] = s[-1]

        for i in range(len(s)-2, -1 ,-1):
            if s[i] > s[arr[i + 1]]:
                arr[i] = i
            else:
                arr[i] = arr[i + 1]

        for i in range(len(s)):
            if s[i] < s[arr[i]]:
                # Swap s[i] with the rightmost max digit
                j = arr[i]
                s[i], s[j] = s[j], s[i]
                break
                
        return int(''.join(s))
        
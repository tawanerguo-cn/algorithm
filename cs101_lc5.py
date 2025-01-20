class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(a, b):
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
            return s[a + 1:b]
        
        r = ""
        for i in range(len(s)):
            x = f(i, i)
            y = f(i, i + 1)
            if len(x) > len(r): r = x
            if len(y) > len(r): r = y
        return r

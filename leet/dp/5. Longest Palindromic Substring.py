class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = ['' for i in range(len(s))]
        for i in range(len(s)):
            odd_pal = self.sub_pal(i, i, s)
            even_pal = self.sub_pal(i, i + 1, s)
            dp[i] = even_pal if len(even_pal) >= len(odd_pal) else odd_pal
        return max(dp, key=len)

    def sub_pal(self, l, r, s):
        tmp = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            tmp = s[l:r + 1]
            l -= 1
            r += 1
        return tmp

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        num_str = ""
        res = re.search(r'(^\d+)|(^-\d+)|(^\+\d+)', s.lstrip())
        if not res:
            return 0
        res = int(res.group())
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < -2 ** 31:
            return -2 ** 31
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        """bbb a.23cbb908.ab!@#$%^&*()"""
        j = 0
        visited = set()
        res = 0

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[j])
                j += 1

            res = max(i - j + 1, res)
            visited.add(s[i])
            print(visited)

        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("bbb a.23cbb908.ab!@#$%^&*()"))

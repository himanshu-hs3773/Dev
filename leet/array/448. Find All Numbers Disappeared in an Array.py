from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        c = 1000000
        for num in nums:
            nums[(num - 1) % c] += c
        return [i + 1 for i, v in enumerate(nums) if v < c]

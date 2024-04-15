from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     while nums[i] != nums[nums[i] - 1]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # return [v for i, v in enumerate(nums) if v != i + 1]
        c, cc = 1000000, 2000000
        for num in nums:
            nums[(num - 1) % c] += c
        return [i + 1 for i, v in enumerate(nums) if v > cc]

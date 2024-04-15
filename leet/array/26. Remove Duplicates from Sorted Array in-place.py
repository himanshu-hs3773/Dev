from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != temp:
                nums[idx] = nums[i]
                idx += 1
                temp = nums[i]
        return idx

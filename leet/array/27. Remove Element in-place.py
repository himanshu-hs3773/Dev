from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[write] = nums[j]
                write += 1
        return write

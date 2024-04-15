from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums[k:] + nums[:k] left rotate
        nums = nums[-k:] + nums[:-k]
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]  # nums[len(nums)-k:] + nums[:len(nums)-k]

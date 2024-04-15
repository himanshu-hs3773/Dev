from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's Voting Algorithm
        count = 0
        candidate = nums[0]
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate = num
            else:
                count -= 1
        return candidate

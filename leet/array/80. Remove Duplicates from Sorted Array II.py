from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp, cnt, idx = nums[0], 1, 1
        for i in range(1, len(nums)):
            if temp != nums[i]:
                nums[idx] = nums[i]
                temp = nums[i]
                idx += 1
                cnt = 1
            elif cnt < 2:
                nums[idx] = nums[i]
                idx += 1
                cnt += 1
        return idx

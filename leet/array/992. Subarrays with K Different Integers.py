from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # def f(k):
        #     pos = [0] * len(nums)
        #     cnt = Counter()
        #     j = 0
        #     for i, x in enumerate(nums):
        #         cnt[x] += 1
        #         while len(cnt) > k:
        #             cnt[nums[j]] -= 1
        #             if cnt[nums[j]] == 0:
        #                 cnt.pop(nums[j])
        #             j += 1
        #         pos[i] = j
        #     return pos

        # return sum(a - b for a, b in zip(f(k - 1), f(k)))
        count = defaultdict(int)
        res = 0
        l_far = l_near = 0
        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[l_near]] -= 1

                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near += 1
                l_far = l_near

            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near += 1

            if len(count) == k:
                res += l_near - l_far + 1
        return res

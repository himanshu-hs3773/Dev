# str1 = "First string"
# str2 = "Second string"
# matched_set = set(str1.split()) & set(str2.split())
# print([s for s in str1.split() if s not in matched_set] + [s for s in str2.split() if s not in matched_set])
# print(matched_set)
#
# n = 2
# my_dict = {"laptop": 999, "smartphone": 999, "smart tv": 500, "smart watch": 300, "smart home": 9999999}
#
# print(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))
# print(sorted(my_dict.items(), key=lambda x: (x[1], x[0]))[n-1][0])
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from typing import Optional, List


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     res = [0] * (n + 1)
#     res[0] = 0
#     res[1] = 1
#     for i in range(2, n + 1):
#         res[i] = res[i - 1] + res[i - 2]
#     return res[n]
#
#
# def fib2(n):
#     memo = {}
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fib2(n-1) + fib2(n-2)
#         return memo[n]
#
#
# print(fib(6))
# print(fib2(6))
# s = "abvcbd"
# print(min(["1w4", "333", "24", "000", "6333", "34"], key=len))

def find_missing(nums):
    # TODO: Write - Your - Code
    total = 0
    max_num = -1
    for n in nums:
        total += n
        if n > max_num:
            max_num = n
    missing = int((max_num ** 2 + max_num) / 2) - total
    return missing if missing else max_num + 1


# e = find_missing([1, 4, 2, 3, 5, 6, 7, 8])
# print(e)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda a, b: a.val < b.val)
        pq = [head for head in lists if head]
        heapify(pq)
        dummy = cur = ListNode()
        while pq:
            node = heappop(pq)
            if node.next:
                heappush(pq, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next


ranked = [100, 100, 99, 99, 99, 80]
temp = -1
i, j = 0, 0
while i < len(ranked):
    if ranked[i] != temp:
        temp = ranked[i]
        ranked[j] = ranked[i]
        j += 1
    i += 1
print(ranked[:j][::-1])

a = [9, 8, 6, 4, 2, 0, -3, -7]
b = [-7, -3, 0, 2, 4, 5, 6, 8, 9]
x = 5
# print(bisect_right(b, x))
# print()

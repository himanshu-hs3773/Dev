import heapq
import math
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # for i in range(len(points)):
    # points[i] = (points[i][0]**2 + points[i][1]**2, [points[i][0], points[i][1]])
    # return [a[1] for a in sorted(points, key=lambda x: x[0])[:k]]

    distances = [0] * len(points)
    for i in range(len(points)):
        # dist = math.sqrt()
        distances[i] = (points[i][0] ** 2 + points[i][1] ** 2, i)

    print(distances)

    heapq.heapify(distances)
    print(distances)
    res = []
    while k and distances:
        _, i = heapq.heappop(distances)
        res.append(points[i])
        k -= 1
    return res


# points = [[3, 3], [5, -1], [-2, 4], [-3, 7], [-2, -4], [-2, 3]]
# k = 2
# print(kClosest(points=points, k=k))

heap = []

# # x = bytearray("sam 12", encoding="utf-8")
# x = bytes("sam 2", encoding="utf-8")
#
# print(x)
# for a in x:
#     print(a, chr(a))
# # for s in "sam":
# #     print(ord(s))

# codeInString = 'a = 8\nb=7\nsum=a+b\nprint("sum =",sum)'
# codeObject = compile(codeInString, 'sumstring', 'exec')
#
# print(codeObject)
# exec(codeObject)
# program = 'a = 5\nb=10\nprint("Sum =", a+b)'
# exec(program)
# # get an entire program as input
# program = input('Enter a program:')
#
# # execute the program
# exec(program)
# print(globals())
# print(locals())
print({True: 1})
# print({{"w", }: 1})
nums = [0, 1, 2, 3, 4]
arr = [0] * len(nums)
print(arr)
print(len(arr))

exit(0)

heapq.heappush(heap, 8)
print(heap)
heapq.heappush(heap, 1)
print(heap)
heapq.heappush(heap, 11)
heapq.heappush(heap, 11)
print(heap)
heapq.heappush(heap, 0)
heapq.heappush(heap, 0)
print(heap)
heapq.heapreplace(heap, 0)
print(heap)

for i in range(9):
    print(heapq.heappop(heap))
    if not heap:
        break

# while heap:
#     print(heapq.heappop(heap))
# print(heap)

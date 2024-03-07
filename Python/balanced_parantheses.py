import collections

n = 2

q = collections.deque()
q.append(('', 0, 0))
res = []

while q:

    print(q)
    node, opn, clse = q.popleft()
    print(q)

    print("Node", '" ', node, ' "', end=" ")
    print("Open :", opn, end=" ")
    print("Close :", clse)

    if opn == clse == n:
        res.append(node)
        print("Result :", res)
        continue

    if opn < n:
        q.append((node + '(', opn + 1, clse))
        print("Queue 1st if:", q)
    if clse < opn:
        q.append((node + ')', opn, clse + 1))
        print("Queue 2nd if:", q)
    print("          ")

print(res)

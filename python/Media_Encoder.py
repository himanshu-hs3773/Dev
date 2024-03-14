from queue import PriorityQueue


def optimalSum(fileSizes: [int]) -> int:
    pq = PriorityQueue()
    computation_sum = 0

    if not len(fileSizes):
        return -1

    for i in fileSizes:
        pq.put(i)

    while len(pq.queue) > 1:
        temp_s = pq.get() + pq.get()
        computation_sum += temp_s
        pq.put(temp_s)

    return computation_sum

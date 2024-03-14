def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(high)


print(quicksort([13, 3]))

def recursive_traverse(lst):
    if not lst:
        return

    print(lst[0])

    recursive_traverse(lst[1:])


my_list = [1, 2, 3, 4, 5]

recursive_traverse(my_list)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))  # Output: 120


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))  # Output: 13


import string


class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def palindrome(word_to_check):
    input_string = Deque()

    for word in word_to_check:
        input_string.add_rear(word.lower())

    print(input_string.items)

    index_front = 0
    index_rear = input_string.size()

    if not input_string.is_empty():
        while index_front <= index_rear:
            if index_front != index_rear:
                k1 = input_string.remove_front()
                k2 = input_string.remove_rear()

                if k1 == k2:
                    index_front += 1
                    index_rear -= 1

                else:
                    return "It's not a Palindrome"

            return "It's a Palindrome"




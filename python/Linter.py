class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def match_symbols(symbol_str):
    openers = ['[', '{', '(']
    closers = [']', '}', ')']

    my_stack = Stack()

    index = 0

    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)

        else:

            if my_stack.is_empty():
                return False

            else:
                top_item = my_stack.pop()
                k1 = openers.index(top_item)
                k2 = closers.index(symbol)
                if k2 != k1:
                    return False

        index += 1

    if my_stack.is_empty():
        return True

    return False


print(match_symbols('{()}'))



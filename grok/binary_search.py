import random


def binary(numbers: list, num):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == num:
            return mid
        if numbers[mid] > num:
            high = mid - 1
        elif numbers[mid] < num:
            low = mid + 1
    return None


def generate_strings():
    def generate_string(length):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        string = ''
        last_char = None
        for _ in range(length):
            char = random.choice(alphabet)
            while char == last_char:
                char = random.choice(alphabet)
            string += char
            last_char = char
        return string

    max_length = 12
    min_length = 4

    string1_length = random.randint(min_length, max_length)
    string2_length = random.randint(min_length, max_length)

    str1 = generate_string(string1_length)
    str2 = generate_string(string2_length)

    return f"{str1} {str2}"


name_list = []
for i in range(10):
    name_list.append(generate_strings())

name_list.append("james adams")

print(sorted(name_list))

print(binary(sorted(name_list), "james adams"))

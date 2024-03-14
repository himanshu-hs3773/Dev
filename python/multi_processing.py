import os
from multiprocessing import Process, current_process


def square(number_):
    result = number_ * number_
    process_id = os.getpid()
    print(f"Process ID: {process_id}")
    print("Process name: ", current_process().name)

    print(f"The number {number_} squares to {result}.")


if __name__ == '__main__':

    processes = []
    numbers = [1, 2, 3, 4]

    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)
        process.start()


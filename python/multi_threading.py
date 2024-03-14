from time import sleep
from threading import *


class Himanshu(Thread):
    def run(self):
        for i in range(2):
            print("Himanshu")
            print(current_thread())
            sleep(1)  # avoiding sync collisions


class Singh(Thread):
    def run(self):
        for i in range(2):
            print("Singh")
            print(current_thread())
            sleep(1)  # avoiding sync collisions


t1 = Himanshu()
t2 = Singh()
print(active_count())
print(current_thread())
t1.start()
sleep(0.2)  # avoiding sync collisions
t2.start()

t1.join()  # used to make Main Thread wait till t1 & t2 are executed
t2.join()
print("That's my name")
print(current_thread())

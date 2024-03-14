from src.utils.logger import info, warning, error, critical  # noqa: F401 pylint: disable=W0611
from collections.abc import Sequence
from typing import TypeAlias

# type Vector = list[float]
Vector: TypeAlias = list[float]

print(type(Vector))


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)


type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]
type Server = tuple[Address, ConnectionOptions]


def broadcast_message_new(message: str, servers: Sequence[Server]) -> None:
    ...


# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message_old(
        message: str,
        servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
    ...


class Base:
    MILES_TO_KM = 1.6

    def __init__(self):
        self.status = 'On'
        self.exit = True

    @staticmethod
    def addition(a, b):
        return a + b

    def myfunc(self):
        self.status = 'Off'
        return

    def new_func(self):
        return self.addition(11, 12)

    @staticmethod
    def method_overloading(a, b, total=False, mult='no', append=0):
        """
            # # Method Overloading
            # obj = Base()
            # print(obj.method_overloading(1, 5))                   -> -4
            # print(obj.method_overloading(1, 5, total=True))       -> 6
            # print(obj.method_overloading(1, 5, mult='yes'))       -> 5
            # print(obj.method_overloading(1, 5, append=1))         -> 15
        """
        if total:
            return a + b
        if mult == 'yes':
            return a * b
        if append > 0:
            return str(a) + str(b)
        return a - b

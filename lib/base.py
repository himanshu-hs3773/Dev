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


class OriginalClass(object):

    def __init__(self):
        self.str = "Zzz"

    def original_func(self):
        print("This's original")


def monkey_patch(self):
    print("This's updated")


obj_OriginalClass = OriginalClass()
obj_OriginalClass.original_func()
OriginalClass.original_func = monkey_patch  # dynamically updating a Class function using monkey patching
obj_OriginalClass.original_func()

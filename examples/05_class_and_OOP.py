class Example:
    def do_nothing(self):  # 'self' is object ref., like 'this' in Java/C#
        pass


class Heritage(Example):
    ...


example = Heritage().do_nothing()


class Polymorphism(Example):
    def do_nothing(self):
        print('Nothing...')


example = Polymorphism().do_nothing()


class Magic():
    def __init__(self):  # like an constructor in Java/C#
        print('Magic!')

    def __repr__(self):  # string reproduction
        return "<class 'Magic'>"

    def __len__(self):  # length result
        return 0

    def __str__(self):  # string convertion
        return 'Magic'


magic = Magic()

print(magic)
length = len(magic)

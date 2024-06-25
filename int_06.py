import inspect

class Test:
    def __init__(self, num_l, num_t):
        self.num_l = num_l
        self.num_t = num_t

    def func(self):
        if len(self.num_l) == len(self.num_t):
            for i in range(len(self.num_l)):
                yield self.num_l[i] * self.num_t[i]


def find_attrs(obj):
    attrs = dir(obj)
    cont = []
    for atr in attrs:
        if atr.startswith('__') and atr.endswith('__'):
            cont.append(atr)
    return cont


def find_methods(obj):
    attrs = dir(obj)
    cont = []
    for atr in attrs:
        if not atr.startswith('__') and not atr.endswith('__'):
            cont.append(atr)
    return cont


def introspection_info(obj):

    print(callable(obj))
    print(
        f'Тип объекта:\n {type(obj)},\n'
        f'Атрибуты объекта:\n {find_attrs(obj)}\n'
        f'Методы объекта:\n {find_methods(obj)}\n'
        f'Модуль объекта:\n {inspect.getmodule(obj)}\n'
        f''
    )
    pass


my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
test = Test(my_list, my_tuple)
result = test.func()


introspection_info(my_list)
introspection_info(my_tuple)
introspection_info(test)
introspection_info(result)
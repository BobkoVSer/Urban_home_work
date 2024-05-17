from pprint import pprint

obj = 42
print(dir(obj))
print(type(obj))
obj_string = 'Hello'
obj_list = [obj, obj_string]
print(list(obj_list))
def introspection_info(obj):
    pass

print(callable(introspection_info))
print(dir(introspection_info))
print(hasattr(introspection_info, 'obj'))





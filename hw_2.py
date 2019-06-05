

def atom(value=None):

    if not value:
        return None

    def get_value():

        nonlocal value
        return value

    def set_value(new_value):

        nonlocal value
        value = new_value
        return value

    def process_value(*args):
        nonlocal value
        for func in args:
            value = func(value)
        return value

    def delete_value():
        nonlocal value
        value = None
        return value

    return get_value, set_value, process_value, delete_value


get_v, set_v, proc_v, del_v = atom(10)

print(get_v())
print(set_v(15))
print(get_v())
print(proc_v(lambda x: x**2, lambda x: x-1))
print(get_v())
print(del_v())
print(get_v())
print(set_v(11))


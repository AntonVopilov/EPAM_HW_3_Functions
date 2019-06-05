
counter_name = 0


def make_it_count(func, counter_name):

    def wrapper(*args):
        global counter_name
        counter_name += 1
        return func(*args)
    return wrapper


new_f = make_it_count(lambda x: x**2, counter_name)

print(new_f)
print(new_f(1))
print(counter_name)

print(new_f(2))
print(counter_name)

print(new_f(3))
print(counter_name)

print(new_f(50))
print(counter_name)
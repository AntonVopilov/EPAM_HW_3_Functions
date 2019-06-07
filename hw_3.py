



def make_it_count(func, counter_name: str):
    def wrapper(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)
    return wrapper

another = 22
new_f = make_it_count(lambda x: x**2, 'another')


print(new_f)
print(new_f(1))
print(another)

print(new_f(2))
print(another)

print(new_f(3))
print(another)

print(new_f(50))
print(another)

pre = 11
new_f = make_it_count(lambda x: x**3, 'pre')
print(new_f(2))
print(pre)
print(new_f(7))
print(pre)
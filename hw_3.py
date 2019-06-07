



def make_it_count(func, counter_name: str):
    globals()[counter_name] += 1
    return func

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

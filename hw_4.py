
def func(*args, **kwargs):
    """my_doc"""

    for arg in args:
        print('arg', arg)

    for name, arg in kwargs.items():
         print(name, arg)
    print('\n')


def modified_func(func, *fixated_args, **fixated_kwargs):

    def wrapper(*args, **kwargs):
        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__

        if not args and not kwargs:
            return func(*fixated_args, **fixated_kwargs)

        union_args = fixated_args
        union_kwargs = fixated_kwargs.copy()

        if args:
            union_args += args
        if kwargs:
            union_kwargs.update(kwargs)
        return func(*union_args, **union_kwargs)

    return wrapper


fixated_args = (1, 2, 3)
fixated_kwargs = dict(first='first_kw_arg', second='second_kw_arg')



new_func = modified_func(func, *fixated_args, **fixated_kwargs)

new_func()
new_func(404, new_arg='new_kw_arg')


new_func()

print(func.__doc__)
print('new_func.__doc__', new_func.__doc__)
print('new_func.__name__', new_func.__name__)

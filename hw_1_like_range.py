
import string

letters = [char for (i,char) in enumerate(string.ascii_lowercase)]


def func(start=None, stop=None, step=1, **kwargs):
    global letters

    if not start:
        return None

    if not stop:
        stop = start
        start = 0

    chars = [char for char in letters]

    for key, value in kwargs.items():
        chars[chars.index(key)] = value

    if step >=0:
        return chars[chars.index(start): chars.index(stop): step]
    if step < 0:
        return chars[chars.index(stop): chars.index(start): step]


print(func('b', 'p', -1,  **{'l': 7, 'c': 'ghh'}))



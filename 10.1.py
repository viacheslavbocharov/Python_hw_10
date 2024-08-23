def pow(x):
    return x ** 2


def some_gen(begin, n, func):
    current = begin
    for _ in range(n):
        yield current
        current = func(current)


gen = some_gen(2, 4, pow)
print(list(gen))

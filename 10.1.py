def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    sequences = []
    sequences.append(begin)
    yield begin

    res = begin
    counter = 1
    while counter < end:
        res = func(res)
        sequences.append(res)
        yield res
        counter += 1


gen = some_gen(2, 4, pow)
print(list(gen))

def add(*args) -> int:
    return sum(args)


print(add(4, 3, 2, 5))


def subtract(*args) -> int:
    subtract = args[0]
    for i in args[1:]:
        subtract -= i
    return subtract


print(subtract(4, 3, 2, 5))
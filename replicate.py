def minmax(x, y):
    if x > y:
        return x, y

    return y, x


def step(x, y):
    if y == 1:
        return 1, x - 1

    return x % y, x // y


def unreplicate(x, y):
    steps = 0
    x, y = minmax(x, y)
    while x > 0 and y > 0 and x != y:
        x, iter_steps = step(x, y)
        y, x = x, y
        steps += iter_steps

    if x == 1 and y == 1:
        return steps

    return None


print(unreplicate(4, 7))
print(unreplicate(2, 4))
print(unreplicate(10**10, (10**10)+1))

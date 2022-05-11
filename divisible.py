from math import sqrt


def factors(x):
    res = set()
    for i in range(1, int(sqrt(x)) + 1):
        if x % i != 0:
            continue

        res.add(i)
        reciprocal = x // i
        if reciprocal != i:
            res.add(reciprocal)

    return res


def factors_in(x, table):
    res = set()
    if x >= len(table) ** 2:
        for y in table:
            if x % y == 0:
                res.add(y)

        return res

    return factors(x) & table.viewkeys()


def tabulate(xs):
    res = {}
    for i, x in enumerate(xs):
        if x not in res:
            res[x] = set()

        res[x].add(i)

    return res


def fast(xs):
    table = tabulate(xs)
    divisors = [None] * len(xs)

    for i in range(len(xs) - 1, -1, -1):
        x = xs[i]

        if divisors[i] is None:
            divisors[i] = set()

        for factor in factors_in(x, table):
            for j in table[factor]:
                if j < i:
                    divisors[i].add(j)

    sum = 0
    for i in range(len(xs) - 1, -1, -1):
        for j in divisors[i]:
            sum += len(divisors[j])

    return sum


print(fast([1, 1, 1]))
print(fast([1, 2, 3, 4, 5, 6]))

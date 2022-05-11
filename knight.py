def int_to_pair(x):
    return (x // 8, x % 8)


def pair_sum(x, y):
    return (x[0] + y[0], x[1] + y[1])


def on_board(x):
    return x[0] >= 0 and x[0] < 8 and x[1] >= 0 and x[1] < 8


def step(x):
    res = set()

    for large_off in [-2, 2]:
        for small_off in [-1, 1]:
            d = pair_sum(x, (large_off, small_off))
            if on_board(d):
                res.add(d)

            d = pair_sum(x, (small_off, large_off))
            if on_board(d):
                res.add(d)

    return res


def step_all(xs):
    res = set()

    for x in xs:
        res |= step(x)

    return res


def dist(src, dst):
    if src == dst:
        return 0

    i = 1
    srcs = set([src])
    dsts = set([dst])
    while True:
        srcs = step_all(srcs)
        if srcs & dsts:
            return i

        i += 1

        dsts = step_all(dsts)
        if srcs & dsts:
            return i

        i += 1


print(dist((0, 0), (7, 7)))

from datetime import datetime


def pentagonal_number(k):
    return int(k * (3 * k - 1) / 2)


def P(goal):
    partitions = [1]
    for n in range(1, goal+1):
        partitions.append(0)

        for k in range(1, n + 1):
            coeff = (-1) ** (k + 1)
            for t in [pentagonal_number(k), pentagonal_number(-k)]:
                if n - t >= 0:
                    partitions[n] = partitions[n] + coeff * partitions[n-t]

    return partitions[-1]


def Q(n):
    # Represent polynomial as a list of coefficients from x^0 to x^n.
    # G_0 = 1
    G = [int(g_pow == 0) for g_pow in range(n + 1)]

    for k in range(1, n):
        # G_k = G_{k-1} * (1 + x^k)
        # This is equivalent to adding G shifted to the right by k to G
        # Ignore powers greater than n since we don't need them.
        G = [
            G[g_pow] if g_pow - k < 0 else G[g_pow] + G[g_pow - k]
            for g_pow in range(n + 1)
        ]

    return G[n]


def q(n):
    # Represent polynomial as a list of coefficients from x^0 to x^n.
    # g_0 = 1
    g = [int(power == 0) for power in range(n + 1)]
    for k in range(1, n):
        for power in range(n, -1, -1):
            if power - k >= 0:
                g[power] = g[power] + g[power - k]

    print(g)
    return g[n]


for i in range(1, 10):
    q(i)

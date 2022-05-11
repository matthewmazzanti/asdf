def pair(x, y):
    x = x - 1
    y = y - 1
    res = (x**2 + 3*x + 2*x*y + y + y**2) / 2

    return res + 1


print(pair(1, 1))
print(pair(3, 2))
print(pair(2, 3))
print(pair(5, 10))

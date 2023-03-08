# x = 5
# y = 10
# z = 20

x, y, z = 5, 16, 20

# print(x,y,z)

# x,y = y,x

# print(x,y,z)

# x += 5    # x = x + 5
# x -= 2    # x = x - 2
# x *= 8    # x = x * 8
# x /= 4    # x = x / 4
# x %= 5    # x = x % 5
# y //=5    # y = y // 5
# y **=5    # y = y ** 5
# y **=z    # y = y ** z


# print(x,y,z)

values = 1, 2, 3

print(values)
print(type(values))

a, b, c = values    # values listesinde 3 eleman olmalı

print(a, b, c)

values2 = 10, 20, 30, 40, 50

q, *w, e = values2

print(q, w, e)

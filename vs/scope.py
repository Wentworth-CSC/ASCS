def swap(x, y):
    x, y = y, x
    return x, y

a = 2
b = 3
print(a, b)
swap(a, b)
print(a, b)
x = swap

print(x(a, b))
print(a, b)



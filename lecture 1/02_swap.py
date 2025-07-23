# swap через временную переменную
a = 2
b = 5

t = a
a = b
b = t

print(a, b)

# swap python style
a = 2
b = 5

a, b = b, a

print(a, b)

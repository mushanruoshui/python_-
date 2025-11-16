a = 1
b = 1
print(a)
print(b)
for i in range(18):
    c = a+b
    b = a
    a = c
    print(c)
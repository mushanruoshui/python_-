num = int(input('num = '))
mun = 0
while num:
    mun = mun*10 + num%10
    num = num // 10
print(mun)
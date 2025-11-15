# 输入一个大于1的正整数，判断其是否素数
num = int(input('输入一个大于1的正整数:'))
end = int(num ** 0.5)
is_prime = True
for i in range(2,end+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
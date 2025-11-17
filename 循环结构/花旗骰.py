# 玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：
# 玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
# 玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
# 玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，
# 如果玩家摇出了 7 点，庄家胜；如果玩家摇出了第
# 一次摇的点数，玩家胜；其他点数玩家继续摇骰子，
# 直到分出胜负
import random
ka_re = 1000
round = 0
si_ri = 0
while 10000 > ka_re > 0:
    print(f'目前赌注为:{ka_re}')
    num = int(input('请输入下注金额:'))
    if num > ka_re:
        print('下注金额大于持有赌注!')
        continue
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    if a + b in [7,11]:
        print(f'玩家第一轮掷出{a+b}点,玩家胜利!')
        ka_re +=num
        round += 1
        si_ri += 1
    elif a + b in [2,3,12]:
        print(f'玩家第一轮掷出{a+b}点,庄家胜利!')
        ka_re -= num
        round += 1
    else:
        c,d = 0,0
        while True:
            n = 0
            c = random.randint(1, 6)
            d = random.randint(1, 6)
            if c+d ==7:
                print(f'玩家第二轮掷出{c+d}点,庄家胜利!')
                ka_re -= num
                round += 1
                break
            elif c+d ==a+b:
                print(f'玩家第二轮掷出{c+d}点,与第一轮相同!玩家胜利!')
                ka_re += num
                round += 1
                si_ri += 1
                break
            else:
                print(f'玩家第二轮掷出{c + d}点,进行重掷')
print(f'一共进行了{round}轮游戏,玩家获胜{si_ri}次!庄家获胜{round-si_ri}次！')
if ka_re >10000:
    print('玩家赌赢了!')
elif ka_re == 0:
    print('玩家破产了')








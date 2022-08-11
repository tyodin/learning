import random

answer = random.randint(1,100)
# answer = 9

def game(guess):
    times = 1
    while (guess != answer) and (times < 7):
        if guess > answer:
            print ('大了大了~~~')
        else:
            print('小了小了~~~')
        times += 1
        print ('第',times,'次,',end='')
        guess = int(input('请重新猜：'))
    # if i == 3:
    if guess == answer:
        print('猜对了哦，撒花撒花~~~')
    else:
        if guess > answer:
            print ('大了大了~~~')
        else:
            print('小了小了~~~')
        print ('机会用完啦~~~')

print ('猜数游戏开始......')
print ('请猜猜我心里想的是哪个数，1到100的整数哦！')
print ('你有7次机会~~~')
guess = int (input('第1次，你猜的是：'))
game(guess)

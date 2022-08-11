# 题目：判断101-200之间有多少个素数，并输出所有素数。

# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
n = 0
for i in range(2, 100):
    for j in range(2, i):
        if (i % j == 0):
            break
            # print(n,'非素数',end=', ')
    else:
            print(i, end=', ')
            n += 1
print('1——100之间共', n, '个素数')




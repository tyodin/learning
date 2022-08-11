# 题目：判断101-200之间有多少个素数，并输出所有素数。

# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
i = 0
for n in range(2,101):
    for k in range(2,n):
        if (n % k == 0):
            break
            # print(n,'非素数',end=', ')
    else:
            print(n,end=', ')
            i += 1
print('1——100之间共',i,'个素数')




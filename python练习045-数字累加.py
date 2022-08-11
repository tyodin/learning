# 题目：统计 1 到 100 之和。
sum = 0
for i in range(1,101):
    sum += i
print('答：1——100的和为',sum,sep="")

"""
#方法2
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print (sum)
"""
p=1
print("第10天吃之前就剩1个桃子")
for i in range(9, 0, -1):
    p=(p + 1)*2
print("第{0}天吃之前还有{1}个桃子".format(i,p))
print("第1天共摘了{0}个桃子".format(p))


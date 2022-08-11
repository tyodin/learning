score = int(input('分数为:'))

level = 'A' if 100>=score>=90 else 'B' if 90>score>=60 else 'C' if 60>score>=0 else print('输入错误')

print (level)
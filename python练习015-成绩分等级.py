# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
n = float(input('分数：'))
if n >= 90:
    print(n,'分，等级：A')
elif n >= 60:
    print(n,'分，等级：B')
else:
    print(n,'分，等级：C')
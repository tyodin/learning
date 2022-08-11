f = open('列出连续整数.txt','w')
n = 0
for n in range(30):
    n += 1
    print (n,end=' ',sep='',file=f)
f.close
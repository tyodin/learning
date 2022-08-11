import itertools
sum = 0
a = [1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum += 1
print('共计',sum,'组',sep="")
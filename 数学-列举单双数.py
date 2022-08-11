'''
n = 1
while True:
    if n % 2 == 1:
        print(n)
    n += 1
    if n > 100:
        break
'''

n = 1
print('1——100中的双数',end='：')
while True:
    if n % 2 == 0:
        print(n,end = ',')
    n += 1
    if n > 100:
        break
        #else:
        #    pass

    # if n % 2 == 1:
    #     print(n, end=',')
    #     n += 1
    # else:
    #     pass
    #     print(n,'为单数')


# for n in range(1,101):
#     if n % 2 == 0:
#         pass
#     else:
#         print(n,end = ',')
# print ('为单数')
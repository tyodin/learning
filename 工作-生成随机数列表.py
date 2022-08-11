import random
# list = [random.randrange(1000) for i in range(10)]
list = random.sample([i for i in range (100)],10)
list.sort(reverse=False)
print (list)
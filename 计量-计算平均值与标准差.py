from statistics import *

print("计算测量数据的平均值")
input_string = input("输入测量数据，以空格间隔：")
data_list = input_string.split()
sum_list = sum(data_list)
avg = sum_list / len(data_list)
print("测量数据个数为：",len(data_list))
print("测量数据的平均值为：",avg)

# print('平均值为','{:0.2f}'.format(mean(data_list)))
# print('标准差为','{:0.2f}'.format(stdev(data_list)))
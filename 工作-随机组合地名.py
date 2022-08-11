# 随机抽取地市
import random
city_list = ['郑州市', '开封市', '洛阳市', '平顶山市', '安阳市', '鹤壁市', '新乡市', '焦作市', '濮阳市',\
           '许昌市','漯河市','三门峡市','南阳市','商丘市','信阳市','周口市','驻马店市','济源市',\
           '巩义市','兰考县','汝州市','滑县','长垣县','邓州市','永城市','固始县','鹿邑县','新蔡县']
num_samples = 10
samples = random.sample(city_list, num_samples)
print(samples)
print(sorted(city_list))
print(city_list[5])#输出第6个市名
print('共',len(city_list),'个市')
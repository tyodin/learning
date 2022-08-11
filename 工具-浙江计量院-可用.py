# -*- encoding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup  # 导入urllib库的request模块
import lxml  # 文档解析器
import os  # os模块就是对操作系统进行操作
import numpy as np  # 列表、字典、字符串等中计算元素重复的次数
import re #正则表达式模块

urls = []
titles = []
# times =[]
# 爬取所有新闻的url和标题，存储在urls和titles中,这里range(1)表示只爬取1页。
# for i in range(2,3):
    # url = 'http://www.zjim.cn/html/xinwendongtai/index_' + str(i) + '.html'
url = 'http://www.zjim.cn/html/xinwendongtai/index.html'# 将xinwendongtai更换为其他栏目名称即可爬取
res = urllib.request.urlopen(url)  # 调用urlopen()从服务器获取网页响应(respone)，其返回的响应是一个实例
html = res.read().decode('utf-8')  # 调用返回响应示例中的read()，可以读取html
soup = BeautifulSoup(html, 'lxml')
result = soup.find_all('div', class_='content-main')
# 和上面的不同，这里要闻在'div,class = list list_1 list_2'中，所以要修改一下。
# print(result)
download_soup = BeautifulSoup(str(result), 'lxml')
# print('---------------------------------------------------------')
# print(download_soup)

# 获取所有链接地址
url_all = download_soup.find_all('a')
for a_url in url_all:
    a_title = a_url.get_text('target')
    # print(a_title)
    # print('---------------------------------------------------------')
    titles.append(a_title)
    a_url = a_url.get('href')
    urls.append(a_url)

# 定义txt存储路径。
picpath = './zhejiangjiliang/'  # 这里我用的是本程序路径，也可改为c盘或d盘等路径。

def txt(name, text):  # 定义函数名

    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    savepath = picpath + name + '.txt'

    file = open(savepath, 'a', encoding='utf-8')  # 因为一个网页里有多个标签p，所以用'a'添加模式
    file.write(text)
    # print(text)
    file.close

# print(urls[1])

for i in range(len(urls)):
# for i in range(1):
    try:
        res = urllib.request.urlopen('http://www.zjim.cn'+urls[i])
        html = res.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        soup = soup.find('div',id = 'articlebody')
        title_0 = soup.find('div',id = 'title')

        print(str(i+1) + 'saved')

        for p in soup.select('p'):

            t = p.get_text()
            t = t.rstrip()
            # print(t)
            txt(titles[i], t)


    except OSError:
        pass  # 如果报错就不管，继续读取下一个url
    continue

# http://www.zjim.cn/html/xinwendongtai/detail_2022_07/13/5054.html
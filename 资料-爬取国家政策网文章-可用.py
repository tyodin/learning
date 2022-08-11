# -*- encoding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup  # 导入urllib库的request模块
# import lxml  # 文档解析器
import os  # os模块就是对操作系统进行操作
import numpy as np  # 列表、字典、字符串等中计算元素重复的次数

urls = []
titles = []
# 爬取所有新闻的url和标题，存储在urls和titles中,这里range(1)表示只爬取1页。
for i in range(1):
    url = 'http://sousuo.gov.cn/column/31421/' + str(i) + '.htm'
    res = urllib.request.urlopen(url)  # 调用urlopen()从服务器获取网页响应(respone)，其返回的响应是一个实例
    html = res.read().decode('utf-8')  # 调用返回响应示例中的read()，可以读取html
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all('div', class_='list list_1 list_2')  # 和上面的不同，这里要闻在'div,class = list list_1 list_2'中，所以要修改一下。
    # print(result)
    download_soup = BeautifulSoup(str(result), 'lxml')
    # print('---------------------------------------------------------')
    print(download_soup)
    url_all = download_soup.find_all('a')
    for a_url in url_all:
        a_title = a_url.get_text('target')
        # print(a_title)
        titles.append(a_title)
        a_url = a_url.get('href')
        urls.append(a_url)

# 定义txt存储路径。
picpath = './newws/'  # 这里我用的是本程序路径，也可改为c盘或d盘等路径。


def txt(name, text):  # 定义函数名
    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    savepath = picpath + name + '.txt'
    file = open(savepath, 'a', encoding='utf-8')  # 因为一个网页里有多个标签p，所以用'a'添加模式
    file.write(text)
    # print(text)
    file.close


# 读取urls中存储的ulrs[i]，爬取文本。
for i in range(len(urls)):
    try:
        res = urllib.request.urlopen(urls[i])
        html = res.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        print(str(i) + 'saved')
        for p in soup.select('p'):
            t = p.get_text()
            txt(titles[i], t)
    except OSError:
        pass  # 如果报错就不管，继续读取下一个url
    continue
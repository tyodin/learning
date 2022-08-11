# -*- encoding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup  # 导入urllib库的request模块
import lxml  # 文档解析器
import os  # os模块就是对操作系统进行操作
import numpy as np  # 列表、字典、字符串等中计算元素重复的次数
import re #正则表达式模块
#-------------------------------------------------------------------------------------------
urls = [] #定义变量urls，类型为列表
titles = [] #定义变量titles，类型为列表
# times =[]
#-------------------------------------------------------------------------------------------
# 爬取所有新闻的url和标题，存储在urls和titles中,这里range(1)表示只爬取1页。
# for i in range(2,3):
    # url = 'http://www.zjim.cn/html/xinwendongtai/index_' + str(i) + '.html'
url = 'http://www.zjim.cn/html/xinwendongtai/index.html' # 变量url获取索引页地址
# 将xinwendongtai更换为其他栏目名称即可爬取其他索引页
res = urllib.request.urlopen(url)  #变量res从服务器获取网页响应的内容
# 调用urlopen()从服务器获取网页响应(respone)，其返回的响应是一个实例
html = res.read().decode('utf-8')  #变量html读取变量res中的内容并进行编码
# 调用返回响应示例中的read()，可以读取html
soup = BeautifulSoup(html, 'lxml') #对变量html使用模块lxml解析，赋予变量soup
result = soup.find_all('div', class_='content-main') #变量result在变量soup中定位class为content-main的div标签
# print(result)
download_soup = BeautifulSoup(str(result), 'lxml')
#将变量result转换为字符串类型，并对变量result使用模块lxml解析，赋予变量download_soup
print(download_soup)
#----------------------------------------------------------------------------------------------------
# 获取所有链接地址
url_all = download_soup.find_all('a') #
for a_url in url_all:
    a_title = a_url.get_text('target')
    # print(a_title)
    titles.append(a_title)
    a_url = a_url.get('href')
    urls.append(a_url)
#-------------------------------------------------------------------------------------------------------
# 定义txt存储路径。
picpath = './zhejiangjiliang/'  # 这里我用的是本程序路径，也可改为c盘或d盘等路径。
def txt(name, text):  # 定义函数txt()
    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    savepath = picpath + name + '.txt'
    file = open(savepath, 'a', encoding='utf-8')  # 因为一个网页里有多个标签p，所以用'a'添加模式
    file.write(text)
    # print(text)
    file.close
#---------------------------------------------------------------------------------------------------------
# 抓取各条新闻网页内的内容
for i in range(len(urls)):# 抓取index页中列出的全部条目
# for i in range(1):# 只抓取第一条
    try:
        res = urllib.request.urlopen('http://www.zjim.cn'+urls[i]) # 生成各条新闻网页地址
        html = res.read().decode('utf-8') #变量res设置文字编码
        soup = BeautifulSoup(html, 'lxml') #对变量html使用模块lxml解析
        soup = soup.find('div',id = 'articlebody') #在变量soup中定位class为articlebody的div标签
        print(str(i+1) + 'saved') # 向用户显示保存的进度
        for page in soup.select('p'): #让变量p在变量soul的p标签中遍历
            t = page.get_text()
            t = t.rstrip()
            # print(t)
            txt(titles[i], t)
    except OSError:
        pass  # 如果报错就不管，继续读取下一个url
    continue

# http://www.zjim.cn/html/xinwendongtai/detail_2022_07/13/5054.html
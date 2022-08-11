# -*- encoding:utf-8 -*-
#------------------------导入模块--------------------------------------------------
import urllib.request
from bs4 import BeautifulSoup  # 导入urllib库的request模块
import lxml  # 文档解析器
import os  # os模块就是对操作系统进行操作
import numpy as np  # 列表、字典、字符串等中计算元素重复的次数
import re #正则表达式模块
#--------------------------定义空列表-----------------------------------------------------
urls = []
titles = []
#----------------------------获取需要的含有标题和链接的内容块----------------------------------
# 爬取所有新闻的url和标题，存储在urls和titles中,这里range(1)表示只爬取1页。
# for i in range(2,11):
#------------------------for缩进开始-----------------------------------
#     url = 'https://www.jsmi.com.cn/c/www/sygzdt_' + str(i) + '.jhtml'
url = 'https://www.jsmi.com.cn/c/www/sygzdt.jhtml'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
result = soup.find_all('li', class_='news_li_table')
# print(result)
download_soup = BeautifulSoup(str(result), 'lxml')
# print('download_soup------------------',download_soup) #已验证，包含名称及地址
#---------------------------把获得的内容块中的标题和链接分别提取出来---------------------------------------------------------
# 获取所有链接地址
url_all = download_soup.find_all('a') # 提取<a>标签中的内容
# url_all =  BeautifulSoup(str(url_all), 'lxml')
# print ('url_all:--------------',url_all)

for a_url in url_all:

    a_title = a_url.get_text(strip = True) #提取url_all中的所有文字，并进行修剪
    titles.append(a_title) #索引页中所有标题写入变量titles

    a_url = a_url.get('href') #获得变量url_all中的所有链接地址（href的内容）
    # print('a_url--------------------',a_url)
    urls.append(a_url) #索引页中所有链接地址写入变量urls
#------------------for缩进结束-----------------------------------------------------
#-----------------------------文件夹及文件的生成及读写----------------------------------------------------
# 定义txt存储路径。
picpath = './jiangsujiliang/'  # 这里我用的是本程序路径，也可改为c盘或d盘等路径。

def txt(name, text):  # 定义函数名

    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    savepath = picpath + name + '.txt'

    file = open(savepath, 'a', encoding='utf-8')  # 因为一个网页里有多个标签p，所以用'a'添加模式
    file.write(text)
    # print(text)
    file.close
#-------------------------------根据获得的链接地址获取各条的具体内容-----------------------------------------------------------------
for i in range(len(urls)):
# for i in range(1):
    try:
        res = urllib.request.urlopen('https://www.jsmi.com.cn'+urls[i]) #把变量urls中的链接地址补齐，由变量res获取链接中的内容
        html = res.read().decode('utf-8') #编码
        soup = BeautifulSoup(html, 'lxml') #lxml处理
        soup = soup.find('div',class_ = 'container-xw')
        print(str(i+1) + 'saved')

        for p in soup.select('p'):
            t = p.get_text()
            txt(titles[i], t)

    except OSError:
        pass  # 如果报错就不管，继续读取下一个url
    continue

#https://www.jsmi.com.cn/c/www/sygzdt.jhtml
#https://www.jsmi.com.cn/c/www/sygzdt/8320.jhtml

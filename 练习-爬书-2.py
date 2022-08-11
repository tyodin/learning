import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
firurl = 'https://www.99csw.com/book/7509/259315.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'} #定义头
r=requests.get(firurl,headers=headers)
r.encoding='utf-8'
# print(r.text) #打印结果hv6j8
mysoup=BeautifulSoup(r.text,'lxml')
mycontent=mysoup.find(id='chaptercontent',class_='content')
print(mycontent.text.replace('　',''))#通过bs4解析的结果将空格去掉

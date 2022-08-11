import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import re

def get_content():
    url_0 = 'https://www.kanunu8.com/book4/8780/194881.html'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}  # 定义头
    page_0 = requests.get(url_0) #, headers=headers
    # txt = requests.get(url).content.decode('gbk')
    page_0.encoding = 'gbk'  # ISO-8859-1
    # print(page_0.encoding)
    print(page_0.text)
    # return (page_0.text)


def reg_content():
    # 指定解析器是lxml或html.parser
    soup = BeautifulSoup(get_content(), 'html.parser')
    # soup = BeautifulSoup(get_content(),'lxml')
    # soup = BeautifulSoup(get_content(),'xml')
    # soup = BeautifulSoup(get_content(),'html5lib')
    book_0 = soup.find('p')
    str_1 = book_0.text
    return str_1
    # book = book_0.find_all('div')
    # print (book[0].text)
    # for t in book:
    #     print(t.text)
    # print(book_0.text.split('\xa0'*4)) #.strip()

    #得到本章标题
    # title = soup.title
    print (soup.title)

    #得到文件头？
    # head = soup.head
    # print (soup.head)

    # title1 = title.find('a')
    # print(str(title.text))
    # result = book_0.text.replace('　', '')  # 通过bs4解析的结果将空格去掉
    # print(result)

def write_content():
    reg_content()
    # open('整本书1.txt', 'a') as f:
    with open('整本书1.txt', 'a', encoding='gbk') as f:
        f.write(reg_content().str_1)


get_content()
reg_content()
write_content()


# mycontent=mysoup.find(id='chaptercontent',class_='content')
# print(mycontent.text.replace('　','')) # 通过bs4解析的结果将空格去掉
#
# from bs4 import BeautifulSoup

"""
import requests
import time
host='https://www.kanunu8.com/'
firurl='https://www.kanunu8.com/files/old/2011/2568/76189.html' #第一章的url
newurl='https://www.kanunu8.com/files/old/2011/2568/76189.html' #新的url
url=newurl # 初始化
session=requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'} #定义头
def mygetcontent(newurl):
    r=session.get(newurl,headers=headers)
    r.encoding = 'gb2312'
    print(r.text) #打印结果

    mysoup=BeautifulSoup(r.text,'lxml')
    mycontent=mysoup.find(id='chaptercontent',class_='content')
    nextcontent=mysoup.find(class_='last')
    title=mysoup.find(class_='title')
    title=title.find('a') #首先获取相应的class内容，过滤掉a标签
    result=mycontent.text.replace('　','') #通过bs4解析的结果将空格去掉
    newurl=host+nextcontent.a.get('href') #下一章的链接
    #print(result)
    print(str(title.text)) #打印标题
    strtotxt(str(title.text),result)  #将结果写入文件
    return newurl
def strtotxt(strtitle,strtxt):
    with open("D:/小说1.txt",'a+',encoding='utf-8') as f:
        f.write('\n')#将标题前后都写入换行
        f.write(strtitle)
        f.write(strtxt)
for i in range(1161):
    url=mygetcontent(newurl=url)
    print('第'+str(i+1)+'章下载完毕')
    time.sleep(0.2)
"""

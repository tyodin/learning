from bs4 import BeautifulSoup
import requests
import time
host='https://www.huixsw.com'
firurl='https://www.huixsw.com/13/read_1.html' #第一章的url
newurl='https://www.huixsw.com/13/read_1.html' #新的url
url=newurl # 初始化
session=requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'} #定义头
def mygetcontent(newurl):
    r=session.get(newurl,headers=headers)
    #print(r.text) #打印结果
    mysoup=BeautifulSoup(r.text,'lxml')
    mycontent=mysoup.find(id='chaptercontent',class_='content')
    nextcontent=mysoup.find(class_='last')
    title=mysoup.find(class_='title')
    title=title.find('a') #首先获取相应的class内容，过滤掉a标签
    result=mycontent.text.replace('                　　天才本站地址：[]s.7777.！无广告！','').replace('　　','\r')#.replace('\r','').replace('\n','')#.replace('    ','  ').replace('\r\n  \r\n  ','') # 通过bs4解析的结果将空格去掉
    newurl=host+nextcontent.a.get('href') #下一章的链接
    #print(result)
    print(str(title.text)) #打印标题
    strtotxt(str(title.text),result)  #将结果写入文件
    return newurl
def strtotxt(strtitle,strtxt):
    with open("D:/小说.txt",'a+',encoding='utf-8') as f:
        # f.write('\n')#将标题前后都写入换行
        f.write(strtitle)
        f.write(strtxt)
for i in range(1161):
    url=mygetcontent(newurl=url)
    print('第'+str(i+1)+'章下载完毕')
    time.sleep(0.2)

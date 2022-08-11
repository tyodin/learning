import os
import time
import requests
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
#selenium路径
path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
head={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
novel_name=input("输入想要下载的小说名字")
#进行自动化操作对笔趣阁进行访问
bro=webdriver.Chrome(executable_path=path)
bro.get('http://www.xbiquge.la/')
search_off=bro.find_element_by_id('wd')
search_off.send_keys(novel_name)#输入小说名字
click_search=bro.find_element_by_id('sss')#找到搜索的位置
click_search.click()#点击搜索
time.sleep(5)
page_text=bro.page_source
bro.quit()
#得到访问页面的源码
tree=etree.HTML(page_text)
novel_name=tree.xpath('//*[@id="checkform"]/table/tbody/tr[2]/td[1]/a/text()')[0]#小说名
url=tree.xpath('//*[@id="checkform"]/table/tbody/tr[2]/td[1]/a/@href')[0]
#访问小说目录页面
response=requests.get(url=url,headers=head)
#因为会存在中文乱码的情况，所以进行下面操作
response.raise_for_status()
response.encoding=response.apparent_encoding
#再进行xpath解析
tree=response.text
tree=etree.HTML(tree)
actor=tree.xpath('//*[@id="info"]/p[1]/text()')[0]#作者名
#创建文件夹
if not os.path.exists('./小说'):
    os.mkdir('./小说')
if not os.path.exists('./小说/'+str(novel_name)):
    os.mkdir('./小说/'+str(novel_name))
urls=[]
zhangjies=tree.xpath('//*[@id="list"]/dl/dd')#获得存放章节信息的列表
for i in zhangjies:
    #把每个章节的url和名字以字典型存放
    zhangjie_name=i.xpath('./a/text()')[0]+'.txt'
    zhangjie_url='http://www.xbiquge.la'+i.xpath('./a/@href')[0]
    dic={
        'name':zhangjie_name,
        'url' :zhangjie_url
    }
    urls.append(dic)
def data_get_write(dic):
    url=dic['url']
    for i in range(20):#因为网站容易崩而出现503页面，故要多次请求
        try:

            data_get=requests.get(url=url,headers=head)
            data_get.raise_for_status()
            data_get.encoding=data_get.apparent_encoding
            data_tree=data_get.text
            break
        except:
            print("请求出错，从新请求")
    data_tree=etree.HTML(data_tree)
    data_writr=data_tree.xpath('//*[@id="content"]/text()')
    with open('./小说/'+str(novel_name)+'/'+dic['name'],'w',encoding='utf-8') as fp:#对小说章节进行持久化存储
        for name in data_writr:
            fp.write(name)
        print(dic['name'],'下载成功！！！')
    #time.sleep(1)
#with ThreadPoolExecutor() as pool:#用进程池访问，因为网站容易崩，所以效率很低
    #pool.map(data_get_write,urls)
for dic in urls:#对每个章节单独访问
    data_get_write(dic)
    time.sleep(1)

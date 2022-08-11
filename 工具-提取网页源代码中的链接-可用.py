# -*- encoding:utf-8 -*-
#提取网页源代码中的链接（磁力也可）

from bs4 import BeautifulSoup
import lxml

urls = []
titles = []
#在此粘贴网页源代码
html_0 = """



"""
soup_0 = BeautifulSoup(html_0, 'lxml')
urls = soup_0.find_all('a' , class_ = 'button is-primary is-fullwidth') #针对不同网页，需要修改此处
for a_url in urls:
    url = a_url.get('href') + '\n'
    print (url)




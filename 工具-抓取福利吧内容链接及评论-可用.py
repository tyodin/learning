# -*- encoding:utf-8 -*-

import urllib.request
# import requests
from bs4 import BeautifulSoup
import lxml
import os
import webbrowser

urls = []
titles = []

headers = {
    "User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }

url ='https://fuliba2022.net/'
index_page = 1 #索引页的页码
# url = 'https://fuliba2022.net/page/' + str (index_page)
res_0 = urllib.request.urlopen(url)
res_0.addheaders = [headers]
# print (res_0.info)
html_0 = res_0.read().decode('utf-8')
# html_0 = html_0.replace(' excerpt-latest', '')
soup_0 = BeautifulSoup(html_0, 'lxml')
for i in range(1, 26):
# for i in range(11, 12):
    result = soup_0.find_all('article', class_='excerpt excerpt-' + str(i))
    download_soup = BeautifulSoup(str(result),'lxml')
    # print (download_soup)
    url_title = download_soup.find_all('h2')
    # print (url_all)
    for a_url_title in url_title:
        a_title = a_url_title.get_text()
        # print (a_title)
        titles.append(a_title)
    url_url = download_soup.find_all('a' , class_ = 'focus')
    for a_url_url in url_url:
        a_url = a_url_url.get('href')
        # print (a_url)
        urls.append(a_url)

picpath = './fuliba/'
def write_file(filename,filetext):
    if not os.path.exists(picpath):
        os.makedirs(picpath)
    savepath = picpath + filename +'.txt'
    file = open(savepath,'a',encoding='utf-8')
    file.write(filetext)
    file.close

# for j in range(len(urls)):
for j in range(1,26):
    try:
        res_1 = urllib.request.urlopen(urls[j])
        html_1 = res_1.read().decode('utf-8')
        soup_1 = BeautifulSoup(html_1, 'lxml')
        soup_content = soup_1.find('article', class_ ='article-content')

        soup_urls = soup_1.find('article', class_ ='article-content')

        soup_comment = soup_1.find('ol', class_ ='commentlist')
        # print ('soup_content:-----------', soup_content)
        # comments = soup_content.get_text()
        # print (comments)
        print(str(j+1) + '已保存') # 向用户显示保存的进度

        def get_url():
            soup_url = soup_urls.find_all('a')
            # print (soup_url)
            for page_url in soup_url:
                # print (page_url)
                text_url = page_url.get('href') + '\n'
                # webbrowser.open(text_url) #使用默认浏览器打开获取的所有链接！！！
                # print (text_url)
                write_file(str(index_page) +'--' + str(j+1) +'--' + titles[j], text_url)
            # else:
            #     continue

        def get_content():
            soup_page = soup_content.find_all('p')
            for page_content in soup_page:
                text_content = page_content.get_text() + '\n'
                text_content = text_content.lstrip()
                write_file(str(index_page) +'--' + str(j+1) +'--' + titles[j], text_content)
            # else:
            #     continue

        def get_comment():
            for page_comment in soup_comment.find_all('p'):
                text_comment = '评论---------：' + page_comment.get_text() + '\n'
                write_file(str(index_page) +'--' + str(j+1) +'--' + titles[j], text_comment)
            # else:
            #     continue


        get_content()
        get_url()

        get_comment()

    except OSError:
        pass  # 如果报错就不管，继续读取下一个url
    continue




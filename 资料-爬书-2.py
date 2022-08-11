import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# Keys 是用作关键词输入
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('log-level=3')
# chrome_options.add_argument("--proxy-server=http://127.0.0.1:1080")
chrome_position = 'F:\\chromedriver\\chromedriver.exe'

class GetBook(object):
    def __init__(self,name):
        self.name = name
        self.books = self.get_book_list()
        self.result = self.get_book_link(self.books,name)
        if self.result == None:
            return
        link_list = self.get_chapter_list(self.result)
        self.get_content(link_list)
    # 获取书名列表
    def get_book_list(self):
        with open('book_list.json','r',encoding='utf-8') as f:
            t = json.load(f)
            return t
    # 获取被查询的图书链接
    def get_book_link(self,books,name):
        for book in books:
            if name == book['name']:
                print(book['link'])
                return book['link']
        print('你所查询的书名不存在！')
        return None
    # 获取章节列表
    def get_chapter_list(self, book_link):
        baseurl = 'http://www.99lib.net'
        proxie = {
            'http': 'http://127.0.0.1:1080',
        }
        print('获取章节列表中...')
        res = requests.get(book_link,proxies=proxie)
        html = BeautifulSoup(res.text, 'html.parser')
        a_list = html.select('#dir')[0].find_all('a')
        link_list = list(map(lambda x: baseurl + x['href'],a_list))
        print('本书共有' + str(len(link_list)) + '章')
        return link_list
    # 获取章节内容
    def get_content(self, link_list):
        driver = webdriver.Chrome(executable_path=chrome_position,chrome_options=chrome_options)
        page = 0
        total = len(link_list)
        for link in link_list:
            page += 1
            driver.get(link)
            # 等待一段时间
            driver.implicitly_wait(1)
            for i in range(40):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(0.02)
            # 找到name为"q"的元素
            elem = driver.find_element_by_id("content").text
            self.save_content(elem, self.name)
            # print(elem.text)
            print('第' + str(page) + '章下载完毕/共' + str(total) + '章')
        print('图书下载完成！')
        driver.quit()
    def save_content(self, content, name):
        with open(name + '.txt', 'a', encoding="utf-8") as f:
            f.write(content + '\n')


if __name__ == '__main__':
    book_name = input('请输入书名:')
    GetBook(book_name)
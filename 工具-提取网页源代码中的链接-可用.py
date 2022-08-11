# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import lxml
import pyperclip
html ="""

"""
# link = 'https://www.meijumi.net/36154.html'
headers = {
    'Cookie': 'td_cookie = 405542359;width = 85 % 25;Hm_lpvt_9352f2494d8aed671d970e0551ae3758 = 1596682842;Hm_lvt_9352f2494d8aed671d970e0551ae3758 = 1596677570',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
}
# html = requests.get(link, headers=headers)
# html =html.text
urls = []
url_list = []
titles = []

soup = BeautifulSoup (html, 'lxml')
urls = soup.find_all('a')
for a_url in urls:
    url = a_url.get('href')
    if url == None:
        continue
    elif url.endswith('pdf'):
        print (url)
        urlhead = 'https://study-cdn.guoch.xyz/Books/%E6%9D%82%E9%A1%B9/%E5%90%BE%E7%88%B1-300%E6%9C%ACPython%E7%94%B5%E5%AD%90%E4%B9%A6/'
        url_list.append(urlhead + url)
url_str = '\n'.join(url_list)
pyperclip.copy(url_str)
import requests
import re
from bs4 import BeautifulSoup

title = []
link = "http://www.paoshu8.com/158_158698/" #索引页
headers = {
    'Cookie': 'td_cookie = 405542359;width = 85 % 25;Hm_lpvt_9352f2494d8aed671d970e0551ae3758 = 1596682842;Hm_lvt_9352f2494d8aed671d970e0551ae3758 = 1596677570',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
}
response = requests.get(link, headers=headers)
# print(response.encoding)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')
soup = str(soup)
# print(html)
# print(soup)
title = re.findall(r'<dt>.*?</dt>', soup)
# print(title)
title = title[1]
title = title.replace('<dt>', '')
title = title.replace('</dt>', '')
title = title.replace('正文', '')
# print(title)
filename = 'D:/novel/' + '%s.txt' % (title)
soup = re.findall(r'<dl>.*?</dl>', soup, re.S)[0]
# print(soup)
zhangjie = re.findall(r'href="(.*?)">(.*?)<', soup)
del zhangjie[0:9]
# print(zhangjie)
for info in zhangjie:
    url, name = info
    # print(info)
    url = 'http://www.paoshu8.com%s' % url
    print('正在下载 %s......' % name)
    with open(filename, 'a+', encoding='gbk') as f:
        chapter_request = requests.get(url)
        chapter_request.encoding = 'utf-8'
        chapter_html = chapter_request.text
        # print(chapter_html)
        chapter_content = re.findall(r'<div id="content">(.*?)</div>', chapter_html)

        chapter_content = str(chapter_content)
        chapter_content = chapter_content.replace('&nbsp;', '')
        chapter_content = chapter_content.replace('<p>', '      ')
        chapter_content = chapter_content.replace('</p>', '\n')
        # chapter_content = chapter_content.replace('\n', '')
        chapter_content = chapter_content.replace(r'\u3000', '')
        chapter_content = chapter_content.replace(r"'", "")
        chapter_content = chapter_content.replace('[', '')
        chapter_content = chapter_content.replace(']', '')
        chapter_content = "".join([s for s in chapter_content.splitlines(True) if s.strip()])  # 去除字符串中的空行

        f.write(name.encode("gbk", 'ignore').decode("gbk", "ignore"))
        f.write('\n')
        f.write(chapter_content.encode("gbk", 'ignore').decode("gbk", "ignore"))
        f.write('\n\n')
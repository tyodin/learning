import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content

if __name__ == '__main__':
    server = 'https://www.xbiquge.so/'
    book_name = '超级电力强国.txt'
    target = 'https://www.xbiquge.so/book/526/'
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
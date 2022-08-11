import requests
import re

url = 'https://www.kanunu8.com/book4/8780/index.html' # 目录页https://www.kanunu8.com/files/old/2011/2447.html
txt = requests.get(url).content.decode('gbk')
m1 = re.compile(r'<td colspan="4" align="center"><strong>(.+)</strong>')
print(m1.findall(txt)[0])
m2 = re.compile(r'<td( width="50%")?><a href="(.+\.html)">(.+)</a>')
raw = m2.findall(txt)
sanguo = []
r_url = 'https://www.kanunu8.com/book4/8780/' #https://www.kanunu8.com/files/old/2011/
for i in raw:
    sanguo.append([i[2], r_url + i[1]])
m3 = re.compile(r'<p>(.+)</p>', re.S)
m4 = re.compile(r'<br />')

# 保存到文件中
with open('整本书.txt', 'a') as f:
    for zj in sanguo:
        zj_url = zj[1]
        print("正在下载----->", zj[0])
        r_nr = requests.get(zj_url).content.decode('gbk')
        n_nr = m3.findall(r_nr)
        f.write('\n' + zj[0] + '\n')
        f.write(m4.sub('', n_nr[0]))
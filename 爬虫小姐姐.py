"""请求网页"""
import requests
import re
import time
import os
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
response = requests.get('https://www.vmgirls.com/13821.html',headers = headers)
# print(response.request.headers)
html = response.text

"""解析网页"""

dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
# print(urls)

"""保存图片"""
for url in urls:
    time.sleep(1)
    #图片的名字
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    # with open(file_name, 'wb') as f:
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)
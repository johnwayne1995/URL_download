#encoding:utf-8
#
#   Author  :   Vicotor
#   E-mail  :   772602479@qq.com
#   Date    :   18/7/20
#   Desc    :   下载图片脚本

import requests
# import codecs

PATH = './imgnet'   #保存图片的路径


# URLS = [
# 'http://i0.sinaimg.cn/lx/zc/p/2008/0701/U2423P8T1D733511F914DT20080701073955.jpg',
# 'https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=17b44aa63a01213fdb3e468e358e5db4/9f510fb30f2442a7439783dad243ad4bd1130237.jpg'
# ]


class Img(object):
    def __init__(self, url):
        self.file_name = url.split('/')[-1]
        self.file_name = self.file_name.split('.jpg')[0]
        self.file_name = self.file_name + '.jpg'
        print(self.file_name)
        self.url = url
        self.path = PATH+'/'+self.file_name

    @property
    def data(self):
        r = requests.get(self.url)
        return r.content

    def save(self):
        with open(self.path, 'wb') as fb:
            fb.write(self.data)

f = open(PATH+"/imgneturl.txt", "r")#图片地址存放在imgneturl.txt
g = f.read()
URLS=g.split('\n')

for i,url in enumerate(URLS):
     try:
         Img(url).save()
         print u'第{}／共{}：{}'.format(i+1, len(URLS), 'sucess')
     except:
         print u'第{}／共{}：{}'.format(i + 1, len(URLS), 'fail')

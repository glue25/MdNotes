'''

'''

import urllib
import re
import chardet   #需要导入这个模块，检测编码格式
import requests
import urllib.request
import time
import multiprocessing
import os
URL = 'https://cn.bing.com/dict/search?q=star'
def LocateWord(URL) :
    print(URL)
    request = urllib.request.Request(URL)
    with urllib.request.urlopen(request) as f :
        html = f.read()#.decode('utf8', 'replace')
    
    encode_type = chardet.detect(html)
    print(encode_type)
    Str = html.decode(encode_type['encoding'])#encode_type['encoding']
    # print(encode_type['encoding'])
    with open('t.html','w', encoding=encode_type['encoding']) as f:
        f.write(Str)
    print(len(Str))
    # print(Str[:100])
    regex = re.compile('https://.*?\.mp\d')
    # print(Str.find('mp3'))
    # RF = regex.findall(Str)
    # print(RF)
    # return RF[0]
# print(LocateWord(URL))
# Download_addres='https://cn.bing.com/th?id=OIP.crvSqk_EQNIj1tEfo1TSjgHaLN&pid=Api&rs=1'
def DownloadFilm(DownloadURL, Filename, Form = '.mp3') :
    f=requests.get(DownloadURL)
    #下载文件
    if Form not in Filename:
        Filename = ''.join((Filename,Form))
    with open(Filename,"wb") as code:
         code.write(f.content)
def DownloadMp3(Word, Dir = '', NoRenewMod = True, TPrint = False) :
    Mp3Filename = ''.join((Dir, Word, '.mp3'))
    if NoRenewMod and os.path.exists(Mp3Filename) :
        pass
    else :
        UrlBingWord = 'https://cn.bing.com/dict/search?q='
        URL = ''.join((UrlBingWord,Word))
        Mp3Url = LocateWord(URL)
        DownloadFilm(DownloadURL = Mp3Url, Filename = Mp3Filename)
        if TPrint :
            print(Word)
        time.sleep(1)


    
def DownloadMp3List(WordList, Dir='',NoRenewMod = True) :
    for i in WordList :
        DownloadMp3(i, Dir, NoRenewMod, TPrint = True)
URL2='https://www.bing.com/dict/search?q=star&go=%E6%90%9C%E7%B4%A2&qs=ds&form=Z9LH5'
LocateWord(URL2)
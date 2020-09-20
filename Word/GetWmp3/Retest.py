import re
import chardet   #需要导入这个模块，检测编码格式
import requests
def LocateAMp3(word) :
    with open('XXX.txt','rb') as f:
        Str = f.read()
        encode_type = chardet.detect(Str)
        Str = Str.decode(encode_type['encoding'])
        print(encode_type['encoding'])
        
    # print(len(Str))
    regex = re.compile('https://.*?\.mp\d')
    RF = regex.findall(Str)
    return RF[0]

# Download_addres='https://cn.bing.com/th?id=OIP.crvSqk_EQNIj1tEfo1TSjgHaLN&pid=Api&rs=1'
def DownloadFilm(Download_addres, Filename, Form) :
    f=requests.get(Download_addres)
    #下载文件
    with open("12.jpeg","wb") as code:
         code.write(f.content)
# result = re.match('https://', Str)
#https://dictionary.blob.core.chinacloudapi.cn/media/audio/tom/81/f3/81F33DF80F223103058020B3D5D6DAF7.mp3
#https://dictionary.blob.core.chinacloudapi.cn/media/audio/tom/99/0a/990AC45DB8F0403793BF8A9615A0F993.mp3

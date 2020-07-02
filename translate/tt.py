k = 'Ro￾bustness'
k = k[2]
with open('tt.txt', 'r', encoding='utf8') as f :
    word = f.read()
    word = word.replace(k+'\n','')
    word = word.replace(' \n','')
    word = word.replace('\n',' ')
    word = word.replace('sssss','\n')
    word = word.replace('fifi','fi')
    word = word.replace('ffff','ff')
    # print(word)
with open('tt2.txt', 'w', encoding='utf8') as f :
    f.write(word)

from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.cn',
    ])
with open('tt2.txt', 'r', encoding='utf8') as f :
    word = f.read()
with open('tt3.txt', 'w', encoding='utf8') as f :
    f.write(translator.translate(word,dest = 'zh-CN').text)
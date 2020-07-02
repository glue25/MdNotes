from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.cn',
    #   'translate.google.co.kr',
    ])
# a = translator.translate('我们是朋友',dest = 'zh-CN')
# print(a.text)
with open('tt2.txt', 'r', encoding='utf8') as f :
    word = f.read()
with open('tt3.txt', 'w', encoding='utf8') as f :
    f.write(translator.translate(word,dest = 'zh-CN').text)
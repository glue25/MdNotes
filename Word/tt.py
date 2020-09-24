
# from itertools import tee
# from itertools import chain

# a = ['abc', 'def', 'ghi']
# b = ['1abc', '1def', '1ghi']
# c = ['2abc', '2def', '2ghi']
# d = chain.from_iterable([a,b,c])
# for i in d :
#     print(i)
with open('Words.txt','r',encoding='utf8') as f :
    with open('Words3.txt', 'w', encoding='utf8') as f2 :
        for i in f :
            f2.write(i.split('  ')[0])
            f2.write('\n')


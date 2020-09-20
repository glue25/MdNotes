
from itertools import tee
from itertools import chain

a = ['abc', 'def', 'ghi']
b = ['1abc', '1def', '1ghi']
c = ['2abc', '2def', '2ghi']
d = chain.from_iterable([a,b,c])
for i in d :
    print(i)



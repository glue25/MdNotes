
''''P3 有序的纸牌'''
#对collections的具体细节还是不了解，可以看看实例
#学到了 __len__(self)，__getitem__(self, position)
# suits='spades diamonds clubs hearts'.split()这行也很好

import collections
from random import choice  #从序列中抽取一个元素
Card=collections.namedtuple('Card',['rank','suit']) #可以构建有少量方法没有方法的类
class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA') #这样写直接就是数据成员
    suits='spades diamonds clubs hearts'.split()  #返回列表
    
    def __init__(self):
        self._cards=[Card(rank = rank,suit = suit) for suit in self.suits  #这样的写法是两者遍历的
                                                   for rank in self.ranks]
        
    def __len__(self):   #看起来是可以由len获取长度
        return len(self._cards)
    
    def __getitem__(self, position): #交由实现了__getitem__，这样切片，迭代什么的都可以实现了
        return self._cards[position]
    

def spades_high(card):
    suit_values=dict(spades=3,hearts=2,diamonds=1,clubs=0)
    rank_value=FrenchDeck.ranks.index(card.rank)
    return  rank_value*len(suit_values)+suit_values[card.suit]
  
def test_function():
    MyCard=FrenchDeck()
    print('=')
    print(Card('7','diamonds'))
    print('=')
    print(len(MyCard))
    print(MyCard[0])
    print(choice(MyCard),choice(MyCard))
    print(MyCard[:3])
    print(Card('7','diamonds') in MyCard)  #只要是迭代的就能用in方法
    print('sort')
    for card in sorted(MyCard,key = spades_high):
        print(card)
    
    
    
test_function()
    
    

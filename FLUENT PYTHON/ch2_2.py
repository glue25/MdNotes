#P21生成器表达式部分代码
#Test2_6()中看起来 生成器推导式确实比较好用

def Test2_5():#P22 2-5
    Chars='abcde'
    print(tuple(ord(Char) for Char in Chars))#(97, 98, 99, 100, 101)
    print((ord(Char) for Char in Chars))#<generator object Test2_5.<locals>.<genexpr> at 0x0000027B95BB9D00>
    #如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外括号（打上括号总是对的吧）
    print(ord(Char) for Char in Chars)#<generator object Test2_5.<locals>.<genexpr> at 0x0000027B95BB9D00>
    #构造array.array需要两个参数，这时括号是必须的
    import array
    A=array.array('I',(ord(Char) for Char in Chars))
    print(A)#array('I', [97, 98, 99, 100, 101])

def Test2_6():
    colors=['black','white']
    sizes=['S','M','L']
    for shirt in ( '%s %s' % (c, s) for c in colors for s in sizes ):
        print(shirt)

Test2_5()
print('='*20)
Test2_6()
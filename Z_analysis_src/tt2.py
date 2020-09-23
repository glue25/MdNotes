
def func(c=0,a=3,b=4):
    print(c)
    print(a)
    print(b)
    print('======')
def f(s, **s1):
    print(s1)
    func(s,s1)

d = {'a':1,'b':2}
d2 = {'a':12}
d3 = {}
# func(**d)
# func(**d2)
# func(**d3)
f(100,a=3,b=4)


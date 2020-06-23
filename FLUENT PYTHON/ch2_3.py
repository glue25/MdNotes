#关于元组
#format用法也要注意,这样就规矩了很多

def func1():
    a,b,*rest=range(5)
    print(type(range(5)))
    print(a)
    print(b)
    print(rest,type(rest))#[2, 3, 4] <class 'list'>

def Test2_8():#关于嵌套元组
    metro_areas=[
        ('Tokyo','JP',36.933,(35.689722,139.691667)),
        ('Delhi NCR','IN',21.935,(28.613889,77.208889)),
        ('sAO pAULO','BR',19.649,(-23.547778,-46.635833))
    ]
    print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        print(fmt.format(name, latitude, longitude))



func1()
print('='*20)
Test2_8()
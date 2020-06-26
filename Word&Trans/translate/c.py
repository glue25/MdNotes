# def f(x,y,z) :
#     if (x > 42)
# 2 z=x+y+w
# 3 else
# 4 z = (((x ^ y) + ((x & y) << 1)) | w) +
# 5 (((x ^ y) + ((x & y) << 1)) & w);
x = 1
y = 5
w = 7
z = (((x ^ y) + ((x & y) << 1)) | w) +(((x ^ y) + ((x & y) << 1)) & w)
print((((x ^ y) + ((x & y) << 1)) & w))
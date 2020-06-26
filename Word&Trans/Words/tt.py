# import sys
# import time
# from concurrent import futures
# def p(i) :
#     time.sleep(10-i)
#     print('in p=====')
#     print(i)
#     return(i)

# # print(res)

# if __name__ == '__main__':
#     with futures.ProcessPoolExecutor(10) as executor : 
#         todo = []
#         for i in range(10) :
#             future = executor.submit(p, i)
#             todo.append(future)
#         results = []
#         print('af submit')
#         for future in futures.as_completed(todo) : 
#             res = future.result()
#             print('res', res)
#             results.append(res)
#         print('='*50)
#         for future in futures.as_completed(todo) : 
#             res = future.result()
#             print('res', res)
#             results.append(res)
           
a = [1,2,3,(4,5),[6,7,8]]
b = a[:]
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
b[3]+=(1,2)
print(id(b[3]))




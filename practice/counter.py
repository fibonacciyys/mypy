def createCounter():
     i=0
     def counter():
          nonlocal i
          i+=1
          return i
     return counter

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
            s_time = time.time()
            print ('began call')
            fn(*args, **kw)
            print('%s executed in %s ms' % (fn.__name__, 1000*(time.time()-s_time)))
            print('end call')
            return fn(*args, **kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

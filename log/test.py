
import time
import log

log.error('line:4 - error test from 0 level')

log.log('line:6 - log test from 0 level')

def some_faulty_func():
    print(543/31)
    log.log('line:10 - log test from some_faulty_func()')
    log.error('line:11 - error test from some_faulty_func()')

def f(n=10000):
    return sum(x for x in range(n))

def f_log(n=10000):
    log.log('just normal log')
    return sum(x for x in range(n))

def f_error(n=10000):
    log.error('loging some errors')
    return sum(x for x in range(n))



t = time.time()
for i in range(10000):
    f()
t1= time.time()-t

t = time.time()
for i in range(10000):
    f_log()
t2= time.time()-t

t = time.time()
for i in range(10000):
    f_error()
t3= time.time()-t

print('f() - ',t1)
print('f_log() - ',t2)
print('f_error() - ',t3)


from threading import Thread,Lock
import time
num = 0
#flag = 1
def work():
	global num
	#mutex.acquire(True)#阻塞上锁
	#global flag
	#if flag == 1:
	for i in range(1000000):
		mutex.acquire(True)
		num += 1
		mutex.release()#释放锁
	#mutex.release()
	print('线程一%d'%num)

def work1():
	global num	#在函数内部修改全局变量要用global声明
	#mutex.acquire(True)
	#while True:
	#	if flag ==2:
	for i in range(1000000):
		mutex.acquire(True)
		num += 1
		#break
	#mutex.release()
		mutex.release()
	print('线程二%d'%num)
mutex = Lock()#创建一把锁
t = Thread(target=work)#创建一个线程
t1 = Thread(target=work1)#创建一个线程
t.start()#创建启动
#time.sleep(10)
t1.start()

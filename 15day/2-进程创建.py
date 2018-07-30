from multiprocessing import Process
import time
def num(arg):
	for i in range(10):
		time.sleep(1)
		print('儿子',arg)
a = Process(target=num,args=('孙子',))
a.start()#开始子进程
a.join()#等待子进程完毕
print('父亲')


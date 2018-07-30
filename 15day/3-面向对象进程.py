from multiprocessing import Process
import time

class num(Process):

	def __init__(self,name):
		super().__init__()#给父类初始化，一定要写
		self.name = name

	def run(self):
		for i in range(10):
			time.sleep(1)
			print('重写run方法%s'%(self.name))

p = num('儿子')
p1 = num('孙子')
p.start()
p1.start()
p1.join()
print('我是主线程(父亲)')

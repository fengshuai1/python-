def w(type):
	def w1(fun):
		def a():
			if type == 1:
				print('王者荣耀')
			elif type == 2:
				print('吃鸡')
			fun()
		return a
	return w1

@w(1)
def b():
	print('不好玩')

@w(2)
def b1():
	print('好玩')
b()
b1()

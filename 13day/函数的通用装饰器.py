def w1(fun):
	def shu(*args,**kwargs):
		print('1')
		return fun(*args,**kwargs)
	return shu

@w1
def test():
	print('haha')

#ret = shu('a','b')
#print(ret)

@w1
def test1():
	print('哈哈')
test1()

@w1
def test2(a):
	print('哈哈啊%s'%a)
test2('hehe')

@w1
def test3():
	return '嘎嘎'
ret = test3()
print(ret)

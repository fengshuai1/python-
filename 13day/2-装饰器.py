def num(fun):
	def inner():
		print('成功')
		fun()
	return inner

@num	#test = w1(test)
def test():
	print('支付')

test()

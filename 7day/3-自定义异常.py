class shou(Exception):
	def __init__(self,a,b):
		self.a = a
		self.b = b
def w():
	try:
		s = input('请输入')
		if s = '老王'
			raise shou(s,'老王')
	except shou as result:
		print('shou:哈哈哈%s,嘿嘿%s'%(result.a,result.b))
	else:
		print('没有')
w()

class dog():
	def __init__(self,name):
		self.__name = name
	def __str__(self):
		return '我的名字%s'%self,name
	def __del__(self):
		print('我要挂了')
	def __xing__(self):
		print('汪')
bai = dog('bai')
#bai1 = bai
del bai
#del bai1
print('dadaada')

class dag():
	__instance = None
	__flag = False
	def __init__(self,name):
		print('init')
		if dag.__flag == False:
			self.name = name
			dag.__flag = True
	def __str__(self):
		print('str')
		return "哈哈哈"
	def __del__(self):
		print('del')
	def __new__(cls,*args,**kwargs):
		print('new')
		if cls.__instance != None:
			return cls.__instance
		else:
			cls.__instance = object.__new__(cls)
		return cls.__instance

a = dag('1')
print(a)
print(id(a))

b = dag('2')
print('b')
print(id(b))

print(a.name)

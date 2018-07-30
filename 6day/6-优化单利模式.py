class dag():
	__instance = None
	def __init__(self):
		print('init')
		self.name = 'tom'
	def __str__(self):
		print('str')
		return "哈哈"
	def __del__(self):
		print('del')
	def __new__(cls):
		print('new')
		if cls.__instance != None:
			return cls.__instance
		else:
			cls.__instance = object.__new__(cls)
		return cls.__instance
a = dag()
print(a)
print(id(a))

b = dag()
print(b)
print(id((b))

c = dag()
print(c)
print(id(c))

class dog():
	__instance = None
	def __new__(cls,*arge,**kwarge):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	def __init__(self,name):
		self.name = name
dog1 = dog('xiaoming')
print(id(dog1))
dog2 = dog('xiaohong')
print(id(dog2))

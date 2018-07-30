class dag():
	__instance = None
	__flag = False
	def __new__(cls):
		if cls.insrance is None:
			cls.instance = super().__new__(cls)
		return cls.instance
		else:
			return cls.instance
a = dag()
print(a)
b =dag()
print(b)

class a(object):
	def __init__(self):
		print('啊哈哈')
		self.name = 'nini'
	def __str__(self):
		print('呵呵呵')
		return 'dsds'
	def __del__(self):
		print('qwqw')
	def __new__(cls):
		print('oooo')
		return object.__new__(cls)

b = a()
print(b)


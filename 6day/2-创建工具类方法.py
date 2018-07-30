class tool():
	count = 0
	def __init__(self):
		tool.count+=1
		self.name = '笔'
	def wark(self):
		print('哈哈哈')
	@classmethod
	def getCount(cls):
		return cls.count
a = tool()
a.wark()
a1 = tool()
a1.wark()
print(tool.getCount())
print(a1.getCount())
	

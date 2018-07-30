class feng:
	def __init__(self,name):
		self.__name = name
	def getname(self):
		return self.__name
	def setname(self,Name):
		if len(Name) <= 2:
			self.__name = Name
		else:
			print('输入有无')
laowang = feng(12434)
print(laowang.getname())



class msg():
	def __amsg(self,money):
		if money > 0:
			print('发短信')
		else:
			print('余额不足')
	def amsg(self,money):
		self.__amsg(money)
a = msg()
a.amsg(10)

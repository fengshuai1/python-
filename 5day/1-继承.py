class ren():
	def __init__(self,name,fang,che):
		self.name = name
		self.fang = fang
		self.che = che
		self.__money = 100
	def getmoney(self):
		return self.__money
	def setmoney(self):
		self.__money = 200
	def __
	def name1(self):
		print('刘彦国')
	def fang1(self):
		print('我没有房')
	def che1(self):
		print('我也没有车')
	def sao(self):
		print('但是，我骚啊!')
	def setName(self,name):
		self.name = name
	def __str__(self):
		msg = '%s\n住的是%s\n开的是%s'%(self.name,self.fang,self.che)
		return msg
class nanren(ren):
	pass
class nvren(ren):
	pass
nan = nanren('冯帅','海南大别墅','兰博基尼')
print(nan)



nan.name1()
nan.fang1()
nan.che1()
nan.sao()
print(nan)
#nv = nvren()
#nv.chi()
#nv.shui()
#nv.shuo()

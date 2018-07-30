class cat():
	def jiao(self):
		print('喵喵')
	def pao(self):
		print('猫会跑')
	def introduce(self):
		print('我的颜色%s 我的名字叫%s 我的大小%s 我的价格%d'%(self.color,self.name,self.size,self.price))
jiamao = cat()
jiamao.jiao()
jiamao.pao()
jiamao.color = '白色'
jiamao.name = '小白'
jiamao.size = 20
jiamao.price = 100
jiamao.introduce()
yemao = cat()
yemao.jiao()
yemao.pao()
yemao.color = '黑色'
yemao.name = '小黑'
yemao.size = 10
yemao.price = 50
yemao.introduce()

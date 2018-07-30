class ren():
	def __init__(self,name,shengao,tizhong):
		self.name = name
		self.shengao = shengao
		self.tizhong = tizhong
	def introduce(self):
		print('我的名字%s\n我的身高%d\n我的体重%d斤'%(self.name,self.shengao,self.tizhong))
nanren = ren('冯',180,130)
nanren.introduce()

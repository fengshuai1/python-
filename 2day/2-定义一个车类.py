class car():
	def pao(self):  #谁调用的就指谁
		print('车会跑')
	def yanse(self):
		print('红色')
	def mingdi(self):
		print('滴滴滴')
a = car()
a.pao()
a.yanse()
a.mingdi()


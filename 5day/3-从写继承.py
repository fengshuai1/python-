class dag():
	def jiao(self):
		print('叫')
class cat(dag):
	def jiao(self):
		print('汪')
class ma(cat):
	def jiao(self):
		print('喵')
a = dag()
b = cat()
c = ma()
a.jiao()
b.jiao()
c.jiao()

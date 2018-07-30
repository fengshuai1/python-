class ren():	#人类
	def __init__(self,name):
		self.name = name
		self.hp = 100

	def naqiang(self,qiang):	#持枪
		self.qiang = qiang

	def zhuanngzidan(self,danjia,zidan):
		danjia,list.append(zidan)	#装子弹

	def zhuangdanjia(self,qiang,danjia):
		qiang.danjia = danjia	#装弹夹

	def zhuangdanjia(self,diren):	#开枪
		zidan = self.qiang.danjia.tanzidan()
		zidan.kill(diren)
		
	#count--伤害量
	def diaoxue(self,count):
		self.hp -= count
		print('还剩多少%d'%self.hp)
		if self.hp <= 0:
			print('挂了')

class qiang():	#枪类
	def __init__(self,name):
		self.name = name
		self.danjia = None


class danjia():	#弹夹类
	def __init__(self,name):
		self,name = name
		self.count = count
		self.list = []	#装子弹

	def tanzidan(self):	#谈子弹
		zidan = self.list.pop()
		return zidan


class zidan():	#子弹类
	def __init__(self,name,kill_count):
		self,name = name
		self.kill_count = kill_count	#子弹伤害

	def kill(self,diren):	#子弹杀人
		diren.diaoxue(self.kill_count)

laowang = ren('老王')	#创建老王
ak47 = qiang('ak47')	#创建枪
danjia = danjia('快速扩容',40)	#创建弹夹 
laowang.naqiang(ak47)	#让老王持枪

for i in range(40):	#创建一些子弹
	zidan = Zidan()
	laowang.zhuangdanjia(danjia,zidan)

laowang.zhuangdanjia(ak47,danjia)	#装弹夹
laosong =ren('老宋')
laowang.opengun(laosong)

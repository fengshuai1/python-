class shu():
	def a(self):
		try:
			a = int(input('请输入一个数'))
	
		except Exception as ret:
			print(ret)
			print('输入错误')
		else:
			print(a+1)
class shu1():
	def a1(self):
		b = input('请输入一个数')
		l = b.isdigit()
		if l == False:
			print('错误')
		else:
			print(int(b)+1)

s = shu()
s.a()
c = shu1()
c.a1()

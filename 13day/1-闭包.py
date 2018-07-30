def num(a,b):
	def shu(x):
		return a*x+b
	return shu
s = num(1,1)
print(s(2))
print(s(3))


def num1(a,b,x):
	return a*x+b

print(num1(1,1,2))
print(num1(1,1,3))

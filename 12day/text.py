def fil(num):
	a,b = 0,1
	print('------1------')
	for i in range(num):
		print('--------2---------')
	temp = yield b
	print('-------3--------')
	print(temp)
	a,b = b,a+b

g = fil(5)
print(g)

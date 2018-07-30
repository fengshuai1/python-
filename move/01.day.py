import os
a = input('请输入文件夹的名字')
b = os.listdir(a)
for i in b:
	position = i.rfind('.')
	c = i[:position]+'呵呵呵呵'+i[position:]
	
	os.rename(b,c)

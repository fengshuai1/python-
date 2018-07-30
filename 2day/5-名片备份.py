import os
def xuan():
	while True:
		print('1:创建文件')
		print('2:备份文件')
		print('3:批量文件重命名')
		print('4:查看文件')
		print('5:删除文件')
		print('6:退出')
		a = int(input('请选择'))
		if a == 1:
			print_1()
def copy():
	name = input('请输入要备份文件名字')
	f = open(name,'r')
	f1 = open(name)
	while True:
		if len(f.read()) == 0:
			break
	content = f.read(1024)
	f1.write(content)
def 

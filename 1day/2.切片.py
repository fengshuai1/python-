name = input('请输入要备份的文件的名字')
f = open(name,'r')
content = f.read()

a = name.rfind('.')
name1 = name[:a] +'back'+ name[a:]

b = open(name1,'w')

while True:
	
	content = f.read(1024)
	if content == "":
		break
	b.write(content)
b.close()
f.close()


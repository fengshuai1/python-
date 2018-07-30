import os
dir_name = input('请输入文件夹的名字')
files = os.listdir(dir_name)

#1-珍藏版.py ---- 1-珍藏版必属精品.py

#os.chdir(dir_name)#改变到movies文件目录
#print(os.getcwd())
'''
for file in files:
	a = file.rfind('.')
	b = file[:a]+'必属精品'+file[a:]
	os.rename(file,b)
'''
for file in files:
	a = file.rfind('.')
	b = file[:a]+'必属精品'+file[a:]
	#movies/01-珍藏版.py
	#movies/01-正藏版必属精品.py
	c = dir_name+'/'+file
	b = dir_name+'/'+b
	os.rename(c,b)

# 学生类
class Student:
	def __init__(self, xuehao, name, age):
		self.xuehao = xuehao
		self.name = name
		self.age = age

	def studentoop(self):
		pass
# 全局变量
new_xuehao = ""
new_name = ""
new_age = ""
 
 # 管理系统类
class Sys:
	def __init__(self):
         pass
 
     # 展示系统菜单
	def show_menu(self):
		print("=" * 56)
		print("                     学生管理系统 v1.0")
		print("                   1:添加用户信息")
		print("                   2:查询用户信息")
		print("                   3:修改用户信息")
		print("                   4:删除用户信息")
		print("                   5:显示用户信息")
		print("                   6:退出系统")
		print("=" * 56)
# 输入学生菜单
	def getinfo(self):
		global new_xuehao
		global new_name
		global new_age
		new_xuehao = input("请输入学号:")
		new_name = input("请输入名字:")
		new_age = input("请输入年龄:")
# 添加学生信息
	def add_stus(self):
#调用getinfo方法
		self.getinfo()
		#以ID为Key,将新输入的信息赋值给Student类
		students[new_xuehao] = Student(new_xuehao,new_name,new_age)
def find_stus(self):
	find_nameId = input("请输入要查的学号")
	if find_nameId in students.keys():
		print("学号:%d\t名字:%s\t年龄:%d"%(students[new_xuehao].xuehao, students[new_xuehao].name, students[new_xuehao].age))
	else:
		print("查无此人")
def alter_stus(self):                                              
	alterId = input("请输入你要修改学生的学号:")                               
	self.getinfo()                                                 
	# 当字典中Key相同时，覆盖掉以前的key值                                        
	if alterId in students.keys():                                 
		students[new_stuId] = Student(new_stuId, new_name, new_age)
		del students[alterId]                                      
	else:                                                          
		print("查无此人")
# 删除学生信息                            
def del_stus(self):                 
	cut_nameID = input("请输入要删除的学号:")
	if cut_nameID in students.keys():
		del students[cut_nameID]    
	else:                           
		print("查无此人")
# 显示学生信息                                                                                
def show_stus(self):

	for new_xuehao in students:

	# print("%s\t%s\t%s" % ("ID:%s"%new_xuehao,"Name:%s"%new_name,"Age:%s"%new_age)) 
		print("ID:%s" % students[new_xuehao].xuehao, "Name:%s" % students[new_xuehao].name,"Age:%s" % students[new_xuehao].age)
# 退出系统                
def exit_stus(self):
	print("欢迎下次使用") 
	exit()
# 创建系统对象                         
sys = Sys()                                                      
# 定义一个容器来存储学生信息                  
students = {}                    
while True:                      
	sys.show_menu()              
	choice = int(input("请选择功能:"))
	if choice == 1:              
		sys.add_stus()           
	elif choice == 2:            
		sys.find_stus()          
	elif choice == 3:            
		sys.alter_stus()         
	elif choice == 4:            
		sys.del_stus()           
	elif choice == 5:            
		sys.show_stus()          
	elif choice == 6:            
		sys.exit_stus()          
	else:                        
		print("您输入有误，请重新输入")

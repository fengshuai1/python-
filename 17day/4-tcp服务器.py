from socket import *
#AF_INET ipv4
s = socket(AF_INET,SOCK_STREAM)

s. bind(('',8889))
print('---111----')
s.listen(5)#监听最大客服端链接数
print('------2222--------')
client,address = s.accept()#等着接电话
print('---3333333--------')
msg = cliten.recv(1024)#接受电话

print(msg.decode('gb2312'))

cliten.close()#关闭

s.close#关闭

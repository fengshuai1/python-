from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.sendto('阿西巴'.encode('gb2312'),('172.20.10.2',8080))
s.close()

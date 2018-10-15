#!/usr/bin/python
#coding=utf-8
from socket import *

def SocketServer():
    try:
        Colon = ServerUrl.find(':')
        IP = ServerUrl[0:Colon]
        Port = int(ServerUrl[Colon+1:])

        #建立socket对象
        print 'Server start:%s'%ServerUrl
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)

        #绑定IP端口号
        sockobj.bind((IP, Port))
        #监听，允许5个连结
        sockobj.listen(5)

        #直到进程结束时才结束循环
        while True:
            #等待client连结
            connection, address = sockobj.accept( )
            print 'Server connected by client:', address
            while True:
                #读取Client消息包内容
                data = connection.recv(1024)
                #如果没有data，跳出循环
                if not data: break
                #发送回复至Client
                RES='200 OK'
                connection.send(RES)
                print 'Receive MSG:%s'%data.strip()
                print 'Send RES:%s\r\n'%RES
            #关闭Socket
            connection.close( )

    except Exception,ex:
        print ex

#ServerUrl = "192.168.16.15:9999"
ServerUrl = "10.89.20.104:9999"
SocketServer()



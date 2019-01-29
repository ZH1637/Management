from socket import *
from select import select

# 准备要关注的IO
server = socket()
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('0.0.0.0',23333))
server.listen(5)

# 添加关注列表
rlist = [server]
wlist = []
xlist = []

while True:
    # 监控IO
    rs, ws, xs = select(rlist,wlist,xlist)
    # 遍历三个列表确定哪个IO发生
    for r in rs:
        # 如果遍历到s,说明s就绪,则有客户端发起连接
        if r is server:
            c,addr = server.accept()
            print('Connect from',addr)
            rlist.append(c)
        # 客户端连接套接字就绪,则接受消息
        else:
            data = r.recv(1024)
            if not data:
                # 客户端退出从列表移除
                rlist.remove(r)
                r.close()
                continue
            print('Receive from %s:%s'%(r.getpeername(),data.decode()))
            r.send(data)
            

    

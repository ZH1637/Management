import show_menu as M
from socket import *
import login as L

client = socket()
client.connect(('127.0.0.1',23333))



def main():
    #  用户登录并显示菜单
    for x in range(3):
        if L.login():
            print('登陆成功!')
            break
        else:
            print('用户名或密码错误!请重新输入!')
            print('您还可以输入%d次!' % (2-x))
            if x == 2:
                return
            continue
    
    # 菜单显示及选择
    while True:    
        M.menu()
        choice = input('请选择>>')
        if not choice:
            client.close()
            return
        client.send(choice.encode())
        data = client.recv(4096)
        
        # 信息接收
        
        print(data.decode())
    
    
        

main()
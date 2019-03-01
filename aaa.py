# from socket import *
# s = socket()
# s.bind(('0.0.0.0',8000))
# s.listen(10)
# fr = open('index.html')
# while True:
#     conn,addr = s.accept()
#     s1 = conn.recv(4096)
#     responseHeaders = "HTTP/1.1 200 OK\r\n"
#     responseHeaders += '\r\n'
#     responseBody = fr.read()
#     response = responseHeaders+responseBody
#     conn.send(response.encode())
#     s2 = conn.recv(4096)
#     print(s2)
import urllib 
import urllib.parse
import urllib.request
s ='%E5%BC%A0%E4%B8%89'
s = urllib.request.unquote(s)


print(s)
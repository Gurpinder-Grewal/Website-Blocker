import os
import time
from datetime import datetime as dt
hostspath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.youtube.com"]
os.chmod(hostspath,777)
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("sorry Not allowed ...")
        with open(hostspath,'w+') as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(hostspath,"w+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list ):
                    file.write(line)
            file.truncate()
        print("Fun hours")    
    time.sleep(5)
        
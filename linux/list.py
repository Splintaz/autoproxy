# Brave Auto Proxy
# Made for Linux. Created by https://github.com/Splintaz
import os

os.system("apt install proxychains")
os.system("wget https://www.proxy-list.download/api/v1/get?type=socks5 -O protosocks5.txt")

breakpoint = 0
breakpoint2 = 0

try:
    while True:
        with open("protosocks5.txt") as f:
            lines = f.readlines()
            ip = lines[breakpoint]
        modip = ip.partition(":")
        sock = "socks5   " + f"{modip[0]}  " + f"{modip[2]}"
        with open("sock5list.txt","a", encoding="utf-8") as socklist:
            socklist.write(f"{sock}")
            socklist.close()
        breakpoint += 1
except:
    print("SOCKS5 list has been created.")
    os.remove("protosocks5.txt")
    try:
        while True:
            with open("/etc/proxychains.conf","a", encoding="utf-8") as proxychains:
                with open("sock5list.txt") as socklist:
                    sockline = socklist.readlines()
                    print(sockline[breakpoint2])
                    proxychains.write(f"{sockline[breakpoint2]}")
                    breakpoint2 += 1
    except:
        os.remove("sock5list.txt")
        exit("SOCKS5 list has been added to proxychains, exiting.")

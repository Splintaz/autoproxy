# Brave Auto Proxy
# Made for Windows. Created by https://github.com/Splintaz
import os
import time
import sys
from winreg import *

breakpoint = 0

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
while True:
    findproxy = find("proxylist.txt", "C:/")
    with open(findproxy) as f:
        lines = f.readlines()
        proxy = lines[breakpoint]
        hostname = lines[breakpoint]
    modname = hostname.partition(":")
    
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "MigrateProxy", 0, REG_SZ, "1")
    SetValueEx(key, "ProxyEnable", 0, REG_SZ, "1")
    SetValueEx(key, "ProxyServer", 0, REG_SZ, f"{proxy}")
    CloseKey(key)

    print(f"New proxy server: {proxy}")

    while True:
        response = os.system("ping " + modname[0])
        if response == 0:
            for remaining in range(75, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Proxy is up, waiting {:2d} seconds before next ping.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            pass
        else:
            print("Proxy is down.")
            breakpoint += 1
            break

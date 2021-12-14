from winreg import *

keyVal = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
try:
    key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
except:
    key = CreateKey(HKEY_CURRENT_USER, keyVal)
SetValueEx(key, "MigrateProxy", 0, REG_SZ, "0")
SetValueEx(key, "ProxyEnable", 0, REG_SZ, "0")
SetValueEx(key, "ProxyServer", 0, REG_SZ, "")
CloseKey(key)

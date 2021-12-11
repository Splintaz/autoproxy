import os
import selenium
import re
from selenium import webdriver
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
brave = find("brave.exe", "C:/")
cd = find("chromedriver.exe","C:/")
print(f"Found Brave: {brave}")
print(f"Found Chromedriver: {cd}")
option = webdriver.ChromeOptions()
option.binary_location = brave
option.add_argument("headless")
try:
    browser = webdriver.Chrome(executable_path=cd, options=option) 
except selenium.common.exceptions.WebDriverException:
    exit("Browser missing, put it in C:/!")
except TypeError:
    exit("Chromedriver missing, put it in C:/!")
browser.get("https://www.proxynova.com/proxy-server-list/elite-proxies/")
rows = len(browser.find_elements_by_xpath("//*[@id='tbl_proxy_list']/tbody/tr"))
columns = len(browser.find_elements_by_xpath("//*[@id='tbl_proxy_list']/thead/tr/th"))
before_XPath = "//*[@id='tbl_proxy_list']/tbody/tr["
aftertd_XPath = "]/td["
aftertr_XPath = "]"
browser.execute_script("window.scrollTo(0, 5000);")
for t_row in range(1, rows):
    for t_column in range(1, columns):
        if t_row != 13:
            FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
            cell = browser.find_element_by_xpath(FinalXPath).text      
            ip = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
            port = r"^\d+$"
            if re.match(str(ip), str(cell)):
                with open("ip.txt","a", encoding="utf-8") as ip:
                    ip.write(f"{cell}\n")
                    ip.close()
            else:
                pass
            if re.match(str(port), str(cell)):
                with open("port.txt","a", encoding="utf-8") as port:
                    port.write(f"{cell}\n")
                    port.close()
            else:
                pass
number = 0
try:
    while True:
        with open("ip.txt") as ip:
            with open("port.txt") as port:
                new_ip = [x[:-1] for x in ip]
                new_port = [x[:-1] for x in port]
                print(f"Added to proxy list: {new_ip[number]}:{new_port[number]}")
                with open("proxylist.txt", "a", encoding="utf-8") as proxylist:
                    proxylist.write(f"{new_ip[number]}:{new_port[number]}\n")
                number += 1
except:
    print("End of line")
    os.remove("ip.txt")
    os.remove("port.txt")

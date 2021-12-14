# Auto Proxy
Installs a list of proxies from your Brave Browser for Windows, while for Linux it fetches proxies from a website where it later adds it to your proxychains configuration file.

<img src="https://raw.githubusercontent.com/Splintaz/autoproxy/main/images/autoproxy.png" width="300" height="300">

# What is Auto Proxy?

Windows: Autoproxy exclusively uses Brave Browser, together with the Chromedriver to utilize Selenium and access your web browser without opening it at all. It installs the list of IPs and ports listed on the website, which it meshes together in order to create you a proxy list. This is an automated task that takes less time than copying the list yourself. After creating the proxy list and running the proxy.py file, it will find the proxy list that you have created. Afterwards it will edit the registry keys in order for you to use it. It will actively ping the proxy server, on which it waits 75 seconds before it executes another ping. 

Linux: Autoproxy uses wget to fetch new data from a website, where it later mashes together to create a new SOCKS5 list. This SOCKS5 list is later appended to your proxychains configuration file. 

<img src="https://raw.githubusercontent.com/Splintaz/braveautoproxy/main/images/splint.png" width="300" height="300">

To find out your Chromedriver version, go to Settings -> About Brave -> Chromium: <your-chromedriver-version>

<img src="https://raw.githubusercontent.com/Splintaz/braveautoproxy/main/images/version.png">

# Windows Instructions

1. Install requirements: pip install -r requirements.txt 
2. Install Brave: https://brave.com
3. Install Chromedriver: https://chromedriver.chromium.org/downloads
4. Run the list.py file.
5. You should now get a proxylist.txt in your directory.
6. Run proxy.py, and it should automatically detect your settings.
 
If the proxy server you are using is not responding, or you wish to remove the proxies absolutely. The "restore.py" file will delete them for you, or you will have to access the registry editor manually.

# Linux Instructions

1. Install requirements: 
* pip install -r requirements.txt
* apt install proxychains 
2. Run the list.py file.
3. You should now have a list of SOCKS5 proxies in your /etc/proxychains.conf 

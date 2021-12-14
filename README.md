# Auto Proxy
Installs a list of proxies from your Brave Browser.

<img src="https://raw.githubusercontent.com/Splintaz/braveautoproxy/main/images/server.png" width="300" height="300">

# What is Auto Proxy?

Autoproxy exclusively uses Brave Browser, together with the Chromedriver to utilize Selenium and access your web browser without opening it at all. It installs the list of IPs and ports listed on the website, which it meshes together in order to create you a proxy list. This is an automated task that takes less time than copying the list yourself.

<img src="https://raw.githubusercontent.com/Splintaz/braveautoproxy/main/images/splint.png" width="300" height="300">

To find out your Chromedriver version, go to Settings -> About Brave -> Chromium: <your-chromedriver-version>

<img src="https://raw.githubusercontent.com/Splintaz/braveautoproxy/main/images/version.png" width="600" height="500">

# Windows Instructions

1. Install requirements: pip install -r requirements.txt 
2. Install Brave: https://brave.com
3. Install Chromedriver: https://chromedriver.chromium.org/downloads
4. Run the .py file
5. You should now get a proxylist.txt in your directory

# Linux Instructions

1. Install requirements: pip install -r requirements.txt 
2. Install Brave: https://brave.com
3. Install Chromedriver: https://chromedriver.chromium.org/downloads
4. Brave should be in /opt/brave.com/brave/brave
5. Chromedriver should be in /usr/bin/chromedriver
6. Do not run as root
7. Run the .py file
8. You should now get a proxylist.txt in your directory

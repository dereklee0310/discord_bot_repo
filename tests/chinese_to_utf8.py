'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-09 00:14:22
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-09 00:49:31
FilePath: \discord_bot_repo\tests\chinese_to_utf8.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
import requests
import urllib
import os

dir = 'C:\\Users\\User\\workspace\\discord_bot_repo\\static\\county_icon' # change this
for file in os.listdir(dir):
    print(os.path.join(dir, file))
    # os.rename(os.path.join(dir, file), os.path.join(dir, urllib.parse.quote(file)))
    os.rename(os.path.join(dir, file), os.path.join(dir, urllib.parse.quote(file).replace('%', '')))
    
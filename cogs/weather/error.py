'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-26 16:19:08
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-27 17:14:54
FilePath: \discord_bot_repo\cogs\weather\error.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''

class WeatherError(Exception):
    pass

class InvalidCountyError(WeatherError):
    '''Raised when the county name is invalid for api'''
    pass
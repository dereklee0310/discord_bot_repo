'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-04 16:53:41
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-06 17:29:13
FilePath: \discord_bot_repo\api_test\weather.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''

import requests
# key: CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC
# Request URL: https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC
# website of data set: https://opendata.cwb.gov.tw/dataset/forecast/F-C0032-001
response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC")
data = response.json()['records']['location']
# print(response.status_code)
# print(type(response))
# print(type(data))

# this function print three sets of weather data
# def print_weather_info(county_name):
#     for i in data:
#         # print(i)
#         print(i['locationName'])
#         for j in i['weatherElement']:
#             # print(j['time'][2])
#             if j['elementName'] == 'Wx':
#                 for k in j['time']:
#                     # print(f"{k['startTime']} ~ {k['endTime'].split(' ')[1]}")
#                     print(f"{k['startTime']} ~ {k['endTime']}")
#                     # print(k['endTime'])
#                     print(k['parameter']['parameterName'])

# print_weather_info('高雄市')


def print_weather_info(county_name):
    print(f"Now Showing: future 36 hours weather forecast")
    for i in data:
        # print(i)
        print(f"                 {i['locationName']}")
        print('-----------------------------------------')
        for j in i['weatherElement']:
            if j['elementName'] == 'Wx':
                for k in j['time']:
                    print(f"{k['startTime']} ~ {k['endTime']}")
                    print(k['parameter']['parameterName'])
        print('-----------------------------------------')

print_weather_info('高雄市')
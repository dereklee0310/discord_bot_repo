'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-02 16:25:49
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-04 23:24:12
FilePath: \discord_bot_repo\api_test\api_test.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-02 16:25:49
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-03 00:44:29
FilePath: \discord_bot_repo\api_test\api_test.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-02 16:25:49
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-03 00:15:52
FilePath: \discord_bot_repo\api_test\api_test.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''

'''
"fields": [
    {
      "id": "sitename",
      "type": "text",
      "info": {
        "label": "測站名稱"
      }
    },
    {
      "id": "county",
      "type": "text",
      "info": {
        "label": "縣市"
      }
    },
    {
      "id": "aqi",
      "type": "text",
      "info": {
        "label": "空氣品質指標"
      }
    },
    {
      "id": "pollutant",
      "type": "text",
      "info": {
        "label": "空氣污染指標物"
      }
    },
    {
      "id": "status",
      "type": "text",
      "info": {
        "label": "狀態"
      }
    },
    {
      "id": "so2",
      "type": "text",
      "info": {
        "label": "二氧化硫(ppb)"
      }
    },
    {
      "id": "co",
      "type": "text",
      "info": {
        "label": "一氧化碳(ppm)"
      }
    },
    {
      "id": "o3",
      "type": "text",
      "info": {
        "label": "臭氧(ppb)"
      }
    },
    {
      "id": "o3_8hr",
      "type": "text",
      "info": {
        "label": "臭氧8小時移動平均(ppb)"
      }
    },
    {
      "id": "pm10",
      "type": "text",
      "info": {
        "label": "懸浮微粒(μg/m3)"
      }
    },
    {
      "id": "pm2.5",
      "type": "text",
      "info": {
        "label": "細懸浮微粒(μg/m3)"
      }
    },
    {
      "id": "no2",
      "type": "text",
      "info": {
        "label": "二氧化氮(ppb)"
      }
    },
    {
      "id": "nox",
      "type": "text",
      "info": {
        "label": "氮氧化物(ppb)"
      }
    },
    {
      "id": "no",
      "type": "text",
      "info": {
        "label": "一氧化氮(ppb)"
      }
    },
    {
      "id": "wind_speed",
      "type": "text",
      "info": {
        "label": "風速(m/sec)"
      }
    },
    {
      "id": "wind_direc",
      "type": "text",
      "info": {
        "label": "風向(degrees)"
      }
    },
    {
      "id": "publishtime",
      "type": "text",
      "info": {
        "label": "資料發布時間"
      }
    },
    {
      "id": "co_8hr",
      "type": "text",
      "info": {
        "label": "一氧化碳8小時移動平均(ppm)"
      }
    },
    {
      "id": "pm2.5_avg",
      "type": "text",
      "info": {
        "label": "細懸浮微粒移動平均值(μg/m3)"
      }
    },
    {
      "id": "pm10_avg",
      "type": "text",
      "info": {
        "label": "懸浮微粒移動平均值(μg/m3)"
      }
    },
    {
      "id": "so2_avg",
      "type": "text",
      "info": {
        "label": "二氧化硫移動平均值(ppb)"
      }
    },
    {
      "id": "longitude",
      "type": "text",
      "info": {
        "label": "經度"
      }
    },
    {
      "id": "latitude",
      "type": "text",
      "info": {
        "label": "緯度"
      }
    },
    {
      "id": "siteid",
      "type": "text",
      "info": {
        "label": "測站編號"
      }
    }

    ############################
    SAMPLE(under ['record']):
    {
      "sitename": "新店",
      "county": "新北市",
      "aqi": "29",
      "pollutant": "",
      "status": "良好",
      "so2": "1.4",
      "co": "0.23",
      "o3": "45",
      "o3_8hr": "31.6",
      "pm10": "20",
      "pm2.5": "10",
      "no2": "9.4",
      "nox": "11.1",
      "no": "1.6",
      "wind_speed": "0.5",
      "wind_direc": "335",
      "publishtime": "2022/07/02 17:00:00",
      "co_8hr": "0.2",
      "pm2.5_avg": "6",
      "pm10_avg": "11",
      "so2_avg": "0",
      "longitude": "121.537778",
      "latitude": "24.977222",
      "siteid": "4"
    },
  ]
'''
import requests

# key: 2e5cd2f6-277b-4252-8639-42ce10cbf84b
# website of data set: https://data.gov.tw/dataset/40448
response = requests.get("https://data.epa.gov.tw/api/v2/aqx_p_432?format=json&api_key=2e5cd2f6-277b-4252-8639-42ce10cbf84b")
aqi = response.json()['records']
# print(response.status_code)
# print(type(response))
# print(type(aqi))

def print_aqi_info(county_name):
    is_time_printed = False
    for i in aqi:
        if i['county'] == new_county:
            # print the title of data
            if not is_time_printed:
                print('--------------------------------------------')
                print(f"| Publish time of AQI: {i['publishtime']} |")
                print('--------------------------------------------')
                is_time_printed = True

            # ignore it if the aqi entry is empty
            if i['aqi'] == '':
                continue

            # print the data, also handle site name like this: 高雄(湖內)站 -> 湖內站
            message = f"  AQI of {i['county']} "
            site_name = i['sitename']
            idx = site_name.find('(')
            if idx == -1:
                message += f"{site_name}"
            else:
                message += f"{site_name.split('(')[1].split(')')[0]}"
            message += f"站:{i['aqi']:>3}, 空氣品質: "
            message += get_air_quality(int(i['aqi']))
            print(message)
    print('--------------------------------------------')

# https://www.xpure-tw.com/blog/vol5_aqipm25
def get_air_quality(aqi):
    if aqi <= 50:
        return "良好"
    elif aqi <= 100:
        return "普通"
    elif aqi <= 150:
        return "對敏感族群不健康"
    elif aqi <= 200:
        return "對所有族群不健康"
    elif aqi <= 300:
        return "非常不健康"
    else:
        return "危害"

# body
county = ""
while True:
    try:
        county = input('Enter the country you live: (e.g. 高雄市): ')
        new_county = county.replace('台', '臺') # convert '台' to '臺' if any
        print_aqi_info(new_county)
    except EOFError:
        break
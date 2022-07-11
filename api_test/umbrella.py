import requests
# key: CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC
# Request URL: https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC&elementName=PoP

# website of data set: https://opendata.cwb.gov.tw/dataset/forecast/F-C0032-001
response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC&elementName=PoP")
data = response.json()['records']['location']

def print_weather_info(county_name):
    print(f"Now Showing: Do you need an umbrella?")
    for i in data:
        # print(f"                 {i['locationName']}")
        print('')
        print('--------------------------------------------------------------------------')
        # print(i['weatherElement'][0]['time'][0])
        percent = int(i['weatherElement'][0]['time'][0]['parameter']['parameterName'])
        msg = f"The Pop(降雨機率) of {i['locationName']}:{percent:>3}%"
        if percent <= 50:
            msg += ' You will most likely not need an umbrella'
        else:
            msg += ' You will most likely need an umbrella'
        print(msg)
        print('--------------------------------------------------------------------------')

print_weather_info('高雄市')
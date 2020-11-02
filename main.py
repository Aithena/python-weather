import urllib.request
import gzip
import json

# 接口地址
city = input('输入城市:')
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city)

def _get():
	data = urllib.request.urlopen(url).read()
	data = gzip.decompress(data).decode('utf-8')
	dict = json.loads(data)
	return dict

def _show(data):
	if data.get('status') == 1002:
		print('Error：您输入的城市有误')
	elif data.get('status') == 1000:
		print('城市：' + data.get('data').get('city'))
		print('温度：' + data.get('data').get('wendu'))
		print('感冒：' + data.get('data').get('ganmao'))
		print('最高温：' + data.get('data').get('forecast')[0].get('high'))
		print('最低温：' + data.get('data').get('forecast')[0].get('low'))
		print('风向：' + data.get('data').get('forecast')[0].get('fengxiang'))
		print('风力：' + data.get('data').get('forecast')[0].get('fengli'))
		print('天气：' + data.get('data').get('forecast')[0].get('type'))
		print('日期：' + data.get('data').get('forecast')[0].get('date'))
		print('-' * 20)

_show(_get())
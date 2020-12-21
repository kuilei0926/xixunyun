import requests
import json

data = {
  "account":"31702160115",
  "password":"160115",
  "school_id":"924",
  "longitude":"114.243681",
  "latitude":"22.696406",
  "address_name":"深圳市朗生建材有限公司"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url='http://xxy.kuileii.cn/release/xixunyun', headers=headers, data=json.dumps(data))
print （json.loads(response.text)）

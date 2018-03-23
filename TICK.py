import requests
import subprocess
from datetime import datetime

request_type = 'POST'
now = datetime.today()
current_date = now.strftime("%Y-%m-%d")
hours_done = '8'

curl_statment = "curl -X POST 'https://digisoft-tv-ltd.tickspot.com/timecard/entries' -H 'Pragma: no-cache' -H 'Origin: https://digisoft-tv-ltd.tickspot.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'X-CSRF-Token: XRhYE+rbAmDJs5AUG/DBRgi2ZtTm3R7VdTligMKk/ySlhuT3kKjK/vMEFgM8beLzQfw82t53j6Gy/PxqEjATvA==' -H 'Accept-Language: en-US,en;q=0.9' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript' -H 'Cache-Control: no-cache' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: _ga=GA1.2.427739848.1514894113; __insp_wid=1721707970; __insp_slim=1514894128455; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9kaWdpc29mdC10di1sdGQudGlja3Nwb3QuY29tLw%3D%3D; __insp_targlpt=VGljayDCuyBkaWdpc29mdC50diBsdGQgwrsgSm9zaCBNb29uZXk%3D; __stripe_mid=e3c3124d-68ab-4637-940c-e9da06f72606; __insp_norec_sess=true; user_id=BAhJIgsyOTE2OTUGOgZFRg%3D%3D--671ce5fb4672c590fc77e1cb1c5aa342dbb4e560; datetime=BAhJIkViMGNjYjkyNTcwMTgxMTRlZmY1MDFjMmIwODM0MmJjODRiNzljMDExNmEzNTA0Zjc1MTU5ZTg2NDJjNDJjOWIxBjoGRUY%3D--cf3440fca78f1c06df4c9e4c6ee5141e910ba9b7; referrer=BAgiKmh0dHBzOi8vZGlnaXNvZnQtdHYtbHRkLnRpY2tzcG90LmNvbS8%3D--fe2060d4e754dd5387970b0bb8b29c503de64ecb; __stripe_sid=8ad52c79-3a2c-4d00-8493-e0474fbf5a9b; _tick_session=QnF6c3dORTlZb3hKQloyNXQ1c3ZmT2JHSDZXekZWeEJCNFJXNFFYRjZ3M1VUOUFnNUR3MTc2UUJqeVVxY3o0VDV2cGJiWDBlRyt1WVEvcGZZUXc4amJ0VVNWM1dWbmxvT2RtOVZMMGUvK2p0VXdTdkI2YWM2eGsycGFORnV3My9zaEFlU3oyeEdFcWhFK1RqVmZVN3Q4WkJGdjRtcGREb1IrcEplVWpGRndNNVdOcDg1bW9pYm9ZaUtJczZqc2pDRllqOFVNdDdJUEtBV081L1FQVkhxTW1rbGNRVklxYkwveVVHMDlFM3QzVnF5MXZsTWJiMDFGdi9DWFdTMjQ5VFNXYSs5UklJVDNZUE0xR1JCNUFsVFE9PS0tRmZLZEVxaWZuTHE4OXc0YXd6SlZHdz09--665ac303b3b71c6c3fdce350db313ade4df8fc58' -H 'Connection: keep-alive' -H 'Referer: https://digisoft-tv-ltd.tickspot.com/' --data 'utf8=%E2%9C%93&entry%5Bid%5D=&timer%5Bid%5D=&entry%5Bdate%5D={WORKING_DATE}&task%5Bid%5D=11012176&entry%5Bhours%5D=8&entry%5Bnotes%5D=&commit=Enter+Time' --compressed"
curl = curl_statment.replace('{WORKING_DATE}', current_date)

url = 'https://digisoft-tv-ltd.tickspot.com/timecard/entries'
cookies = {
    '_ga': 'GA1.2.427739848.1514894113',
    '__insp_wid': '1721707970',
    '__insp_slim': '1514894128455',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly9kaWdpc29mdC10di1sdGQudGlja3Nwb3QuY29tLw%3D%3D',
    '__insp_targlpt': 'VGljayDCuyBkaWdpc29mdC50diBsdGQgwrsgSm9zaCBNb29uZXk%3D',
    '__stripe_mid': 'e3c3124d-68ab-4637-940c-e9da06f72606',
    '__insp_norec_sess': 'true',
    'user_id': 'BAhJIgsyOTE2OTUGOgZFRg%3D%3D--671ce5fb4672c590fc77e1cb1c5aa342dbb4e560',
    'datetime': 'BAhJIkViMGNjYjkyNTcwMTgxMTRlZmY1MDFjMmIwODM0MmJjODRiNzljMDExNmEzNTA0Zjc1MTU5ZTg2NDJjNDJjOWIxBjoGRUY%3D--cf3440fca78f1c06df4c9e4c6ee5141e910ba9b7',
    'referrer': 'BAgiKmh0dHBzOi8vZGlnaXNvZnQtdHYtbHRkLnRpY2tzcG90LmNvbS8%3D--fe2060d4e754dd5387970b0bb8b29c503de64ecb',
    '__stripe_sid': '8ad52c79-3a2c-4d00-8493-e0474fbf5a9b',
    '_tick_session': 'QnF6c3dORTlZb3hKQloyNXQ1c3ZmT2JHSDZXekZWeEJCNFJXNFFYRjZ3M1VUOUFnNUR3MTc2UUJqeVVxY3o0VDV2cGJiWDBlRyt1WVEvcGZZUXc4amJ0VVNWM1dWbmxvT2RtOVZMMGUvK2p0VXdTdkI2YWM2eGsycGFORnV3My9zaEFlU3oyeEdFcWhFK1RqVmZVN3Q4WkJGdjRtcGREb1IrcEplVWpGRndNNVdOcDg1bW9pYm9ZaUtJczZqc2pDRllqOFVNdDdJUEtBV081L1FQVkhxTW1rbGNRVklxYkwveVVHMDlFM3QzVnF5MXZsTWJiMDFGdi9DWFdTMjQ5VFNXYSs5UklJVDNZUE0xR1JCNUFsVFE9PS0tRmZLZEVxaWZuTHE4OXc0YXd6SlZHdz09--665ac303b3b71c6c3fdce350db313ade4df8fc58',}
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://digisoft-tv-ltd.tickspot.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRF-Token': 'XRhYE+rbAmDJs5AUG/DBRgi2ZtTm3R7VdTligMKk/ySlhuT3kKjK/vMEFgM8beLzQfw82t53j6Gy/PxqEjATvA==',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://digisoft-tv-ltd.tickspot.com/',}
data = [
  ('utf8', '\u2713'),
  ('entry[id]', ''),
  ('timer[id]', ''),
  ('entry[date]', current_date),
  ('task[id]', '11012176'),
  ('entry[hours]', hours_done),
  ('entry[notes]', ''),
  ('commit', 'Enter Time'),
  ]

response = requests.post(url, headers=headers, cookies=cookies, data=data)
print response
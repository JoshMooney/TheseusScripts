"""
"   Created by: Josh on 27/03/18
"""

import urllib
import os
import requests


img_path = '/home/josh'
xbox_path = 'XboxApi/imgs'

headers = { 'X-AUTH': '176c920e9db3e9305fec3b2303ecb5ca525e3924', }
xbox_api_url = 'https://xboxapi.com/v2'
response = requests.get(xbox_api_url + '/accountXuid', headers=headers)
res_json = response.json()

xuid = res_json['xuid']
url = xbox_api_url +'/'+ str(xuid) +'/'+ 'screenshots'
response = requests.get(url, headers=headers)
screenshots = response.json()

default_path = os.getcwd()
path = os.path.join(img_path, xbox_path)

if not os.path.exists(path):
    os.makedirs(path)

os.chdir(path)

image_count, download_count = 0, 0
for image in screenshots:
    image_count += 0
    try:
        name = image['titleName'] + "_" + image['deviceType'] + "_" + image['dateTaken'] + '.png'
        if not os.path.isfile(name):
            for i in image['screenshotUris']:
                url = i['uri'].replace('\\', '')
                urllib.request.urlretrieve(url, name)
                download_count += 1
    except Exception as err:
        print(err)

os.chdir(default_path)
print("-- RESULTS -- \n"
      "Image directory: {{DIRECTORY}} \n"
      "* {{TOTAL}} images processed \n"
      "* {{DOWNLOADED}} new images \n"
      "* {{DIFF}} images skipped \n")








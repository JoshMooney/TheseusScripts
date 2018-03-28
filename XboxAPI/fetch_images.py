"""
"   Created by: Josh on 27/03/18
"""
import urllib
import os
import requests
import time
from datetime import datetime

from config import XBOX_API_CONFIG


timestamp = datetime.now()
start_time = time.time()

headers = { 'X-AUTH': XBOX_API_CONFIG._KEY, }
response = requests.get(XBOX_API_CONFIG._API_URL + '/accountXuid', headers=headers)
res_json = response.json()

xuid = res_json['xuid']
url = XBOX_API_CONFIG._API_URL +'/'+ str(xuid) +'/'+ 'screenshots'
response = requests.get(url, headers=headers)
screenshots = response.json()

default_path = os.getcwd()
path = os.path.join(XBOX_API_CONFIG._ROOT_DIRECTORY, XBOX_API_CONFIG._IMG_DIR)

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

process_time = time.time() - start_time
os.chdir(default_path)
print(XBOX_API_CONFIG._IMG_RESPONSE_MSG.replace("{{DIRECTORY}}", path)
                                        .replace("{{TIMESTAMP}}", timestamp)
                                        .replace("{{RUN_TIME}}", process_time)
                                        .replace("{{TOTAL}}", image_count)
                                        .replace("{{DOWNLOADED}}", download_count)
                                        .replace("{{DIFF}}", image_count - download_count))








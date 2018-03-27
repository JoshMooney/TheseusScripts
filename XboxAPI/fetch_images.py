"""
"   Created by: Josh on 27/03/18
"""

from xboxapi import Client
import urllib
import requests

client = Client(api_key="3215f62d3a4226efbf28be18ac9e3b33549e9865")

# g_Josh = client.gamer('Joshmoo2012')
# presence = g_Josh.get('presence')
# xuid = presence['xuid']
#
# screenshots = g_Josh.get('screenshots')

mock_screen_shot = [
                  {
                        "screenshotId": "9c8b5bd0-ff8b-4d08-9b46-9a68763cd558",
                        "resolutionHeight": 2160,
                        "resolutionWidth": 3840,
                        "state": "Published",
                        "datePublished": "2018-03-12T23:13:00.0531057Z",
                        "dateTaken": "2018-03-12 23:12:38",
                        "lastModified": "2018-03-12T23:12:38Z",
                        "userCaption": "",
                        "type": "UserGenerated",
                        "scid": "d1adc8aa-0a31-4407-90f2-7e9b54b0347c",
                        "titleId": 927474846,
                        "rating": 0,
                        "ratingCount": 0,
                        "views": 0,
                        "titleData": "",
                        "systemProperties": "1504bffb-dc80-4bc9-9459-4d5795a12ec20;",
                        "savedByUser": True,
                        "achievementId": "",
                        "greatestMomentId": None,
                        "thumbnails": [{
                            "uri": "https:\/\/screenshotscontent-t3002.xboxlive.com\/xuid-2533274851696933-public\/9c8b5bd0-ff8b-4d08-9b46-9a68763cd558_Thumbnail.PNG",
                            "fileSize": 0,
                            "thumbnailType": "Small"
                        }, {
                            "uri": "https:\/\/screenshotscontent-t3002.xboxlive.com\/xuid-2533274851696933-public\/9c8b5bd0-ff8b-4d08-9b46-9a68763cd558_Thumbnail.PNG",
                            "fileSize": 0,
                            "thumbnailType": "Large"
                        }],
                        "screenshotUris": [{
                            "uri": "https:\/\/screenshotscontent-d3002.xboxlive.com\/xuid-2533274851696933-private\/9c8b5bd0-ff8b-4d08-9b46-9a68763cd558.PNG?sv=2015-12-11&sr=b&si=DefaultAccess&sig=9pAQhAPT3O3SA78DitaCwTipkcpjtitxNyqzwELhKO0%3D",
                            "fileSize": 6791924,
                            "uriType": "Download",
                            "expiration": "2018-03-27 17:43:59"
                        }],
                        "xuid": 2533274851696933,
                        "screenshotName": "",
                        "titleName": "Firewatch",
                        "screenshotLocale": "en-IE",
                        "screenshotContentAttributes": "None",
                        "deviceType": "Scorpio",
                        "screenshotDetails": "https:\/\/xboxapi.com\/v2\/2533274851696933\/screenshot-details\/d1adc8aa-0a31-4407-90f2-7e9b54b0347c\/9c8b5bd0-ff8b-4d08-9b46-9a68763cd558"
                    }]

for image in mock_screen_shot:
    name = image['titleName'] + "_" + image['deviceType'] + "_" + image['dateTaken'] + '.png'
    for i in image['screenshotUris']:
        with open('pic1.jpg', 'wb') as handle:
            response = requests.get(i['uri'], stream=True)

            if not response.ok:
                print
                response

            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)

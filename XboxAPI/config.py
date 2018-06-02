"""
"   Created by: Josh on 28/03/18
"""
import requests

class XBOX_API_CONFIG(object):
    _API_URL = 'https://xboxapi.com/v2'
    _XUID = 2533274851696933
    _ROOT_DIRECTORY = '/home/josh'
    _LOG_DIR = 'XboxApi/logs'
    _IMG_DIR = 'XboxApi/imgs'
    _CLIP_DIR = 'XboxApi/clips'
    _KEY = 'ff54cea91a150f202ff7951cad47ff5b027f46b9'
    _IMG_RESPONSE_MSG = "-- Finished --\n Image directory: {{DIRECTORY}}\n  Timestamp: {{TIMESTAMP}}\n  Process Time: {{RUN_TIME}}\n * {{TOTAL}} images processed \n * {{DOWNLOADED}} new images \n * {{DIFF}} images skipped \n"
    _CLIP_RESPONSE_MSG = "-- Finished --\n Clip directory: {{DIRECTORY}}\n  Timestamp: {{TIMESTAMP}}\n  Process Time: {{RUN_TIME}}\n * {{TOTAL}} clips processed \n * {{DOWNLOADED}} new clips \n * {{DIFF}} clips skipped \n"

    _JOSH_GAMERTAG = 'Joshmoo2012'
    _JACK_GAMERTAG = 'xXxSausageShark'


def get_session():
    _session = requests.session()
    headers = {
        'X-AUTH': XBOX_API_CONFIG._KEY,
    }

    _session.headers.update(headers)
    return _session


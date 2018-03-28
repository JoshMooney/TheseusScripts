"""
"   Created by: Josh on 28/03/18
"""

class XBOX_API_CONFIG(object):
    _API_URL = 'https://xboxapi.com/v2'
    _ROOT_DIRECTORY = '/home/josh'
    _LOG_DIR = 'XboxApi/logs'
    _IMG_DIR = 'XboxApi/imgs'
    _KEY = 'ff54cea91a150f202ff7951cad47ff5b027f46b9'
    _IMG_RESPONSE_MSG = "-- Finished --\n Image directory: {{DIRECTORY}}\n  Timestamp: {{TIMESTAMP}}\n  Process Time: {{RUN_TIME}}\n * {{TOTAL}} images processed \n * {{DOWNLOADED}} new images \n * {{DIFF}} images skipped \n"
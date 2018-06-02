"""
"   Created by: Josh on 27/03/18
"""
import urllib
import os
import requests
import time
from datetime import datetime

from abc import ABCMeta, abstractclassmethod, abstractmethod
from config import XBOX_API_CONFIG, get_session


class BackupAsset:
    def __init__(self):
        self.timestamp = datetime.now()
        self.start_time = time.time()
        self.session = get_session()

        self.processed = 0
        self.downloaded = 0

    def get_xuid(self):
        #return self.session.get(XBOX_API_CONFIG._API_URL + '/xuid/' + XBOX_API_CONFIG._JOSH_GAMERTAG).json()
        return XBOX_API_CONFIG._XUID

    @abstractmethod
    def do_backup(self):
        pass

    def get_path(self, dir):
        return os.path.join(XBOX_API_CONFIG._ROOT_DIRECTORY, dir)

    def change_output_directory(self, dir):
        self.default_path = os.getcwd()
        self.backup_path = os.path.join(XBOX_API_CONFIG._ROOT_DIRECTORY, dir)

        if not os.path.exists(self.backup_path):
            os.makedirs(self.backup_path)
        os.chdir(self.backup_path)

    def revert_directory(self):
        os.chdir(self.default_path)

    def download_assets(self, data, file_ext, date_field, uri_field):
        self.start_time = time.time()
        for asset in data:
            self.processed += 1
            try:
                name = asset['titleName'] + "_" + asset['deviceType'] + "_" + asset[date_field] + file_ext
                if not os.path.isfile(name):
                    for i in asset[uri_field]:
                        url = i['uri'].replace('\\', '')
                        urllib.request.urlretrieve(url, name)
                        self.downloaded += 1
            except Exception as err:
                print(err)
        self.process_time = time.time() - self.start_time

    def log(self):
        log = dict()
        log['directory'] = self.backup_path
        log['timestamp'] = str(self.timestamp)
        log['process_time'] = str(self.process_time)
        log['processed'] = str(self.processed)
        log['downloaded'] = str(self.downloaded)
        log['skipped'] = str(self.processed - self.downloaded)
        return log

class BackupImage(BackupAsset):
    file_extension = '.png'
    date_field = 'dateTaken'
    uri_field = 'screenshotUris'

    def do_backup(self):
        xuid = self.get_xuid()
        url = '/'.join([XBOX_API_CONFIG._API_URL, str(xuid), 'screenshots'])
        response = self.session.get(url)
        screenshots = response.json()

        self.change_output_directory(XBOX_API_CONFIG._IMG_DIR)
        self._download_asset(screenshots)

        self.revert_directory()

    def _download_asset(self, data):
        self.download_assets(data, self.file_extension, self.date_field, self.uri_field)

class BackupClip(BackupAsset):
    file_extension = '.mp4'
    date_field = 'dateRecorded'
    uri_field = 'gameClipUris'

    def do_backup(self):
        xuid = self.get_xuid()
        url = '/'.join([XBOX_API_CONFIG._API_URL, str(xuid), 'game-clips'])
        response = self.session.get(url)
        clips = response.json()

        self.change_output_directory(XBOX_API_CONFIG._CLIP_DIR)
        self._download_asset(clips)

        self.revert_directory()

    def _download_asset(self, data):
        self.download_assets(data, self.file_extension, self.date_field, self.uri_field)

img_bc = BackupImage()
img_bc.do_backup()
log_dir = os.path.join([XBOX_API_CONFIG._ROOT_DIRECTORY, _LOG_DIR, 'image_backup_log.txt'])
with open(log_dir, 'a') as file:
    file.write(img_bc.log())

clip_bc = BackupClip()
clip_bc.do_backup()
log_dir = os.path.join([XBOX_API_CONFIG._ROOT_DIRECTORY, _LOG_DIR, 'clip_backup_log.txt'])
with open(log_dir, 'a') as file:
    file.write(clip_bc.log())








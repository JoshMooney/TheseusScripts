from __future__ import unicode_literals
import youtube_dl
import os, errno

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

song = "https://www.youtube.com/watch?v=LlU4FuIJT2k"

def get_info(url):
    ydl = youtube_dl.YoutubeDL()
    with ydl:
        r = ydl.extract_info(url, download=False)

    if r['_type'] == 'playlist':
        playlist_info = dict()
        playlist_info['Name'] = r['title']
        playlist_info['entries'] = []
        for entry in r['entries']:
            title = dict()
            title['alt_title'] = entry['alt_title']
            title['creator'] = entry['creator']
            title['tags'] = entry['tags']
            title['title'] = entry['title']
            playlist_info['entries'].append(title)
        return playlist_info
    else:
        print("Title was a song")
        song_info = dict()
        return song_info

def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

playlist = 'https://www.youtube.com/playlist?list=PLLwVEplZMU6mgNIJBEmDqsk6Fl8B855xU'
info = get_info(playlist)
cwd = os.getcwd() + '/' + info['Name']
print cwd
try:
    os.makedirs(cwd)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

os.chdir(cwd)
download(playlist)

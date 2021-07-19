"""
Simple Youtube scraper to run with python3
"""
from __future__ import unicode_literals
import youtube_dl


def downloadAudio(input_url):
    # Download Audio input highest quality
    targetURL = input_url
    downloadAudioOptions = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(downloadAudioOptions) as ydl:
        ydl.download([targetURL])
    return


def downloadVideo(input_url):
    # Download a video highest quality
    targetURL = input_url
    downloadVideoOptions = {}
    with youtube_dl.YoutubeDL(downloadVideoOptions) as ydl:
        ydl.download([targetURL])
    return

user_input = input("Please paste Url: ")
type_input = input("Enter 1 for Audio, Enter 2 for Video: ")

if type_input == "1":
    downloadAudio(user_input)
else:
    downloadVideo(user_input)
    


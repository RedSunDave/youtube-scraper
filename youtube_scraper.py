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
    # Download a video in the same way
    targetURL = input_url
    downloadVideoOptions = {}
    with youtube_dl.YoutubeDL(downloadVideoOptions) as ydl:
        ydl.download([targetURL])
    return

user_input = input("Input Url: ")
downloadAudio(user_input)
#if __name__ == "__main__:":
    


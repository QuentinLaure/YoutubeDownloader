import os

from pytube import Playlist
from pytube import YouTube

OUTPUT_PATH = "Musiques_DL"
DOWNLOADED_TITLES = os.listdir(OUTPUT_PATH)  # Titles already in folder without .mp3 extension

def download(link):
    yt = YouTube(link)

    filename = getFileName(yt)
    if (filename in DOWNLOADED_TITLES):
        print("Already downloaded: " + filename)
        return

    # Getting the audio
    audio = yt.streams.get_audio_only()

    audio.download(output_path=OUTPUT_PATH, filename=filename, max_retries=5)
    print("Download completed : " + filename)
    DOWNLOADED_TITLES.append(filename)


def getFileName(yt):
    title_corrected = yt.title
    author_corrected = yt.author
    filename = author_corrected + " - " + title_corrected + ".mp3"
    filename = get_valid_filename(filename)
    return filename


def read_txt(fileName):
    listUrl = []
    lines = open(fileName, 'r').read().split('\n')
    for line in lines:
        url = line.replace("https", "http")
        listUrl.append(url)
    return listUrl


def get_valid_filename(filename):
    invalid = '<>:"/\|?*'
    for char in invalid:
        filename = filename.replace(char, '')
    return filename


if __name__ == '__main__':

    playlistUrl = input("Enter playlist URL. \n")

    print("INPUT = {}".format(playlistUrl))
    playlist = Playlist(playlistUrl)
    print("About to download {} songs from urls : {}".format(playlist.length, playlist))
    # playlist = Playlist("https://music.youtube.com/playlist?list=PLE5-6jx40-23WxlgsX-dkSUvYifIvvV5D")
    # playlist = read_txt("ToDL.txt")  # only for debug purpose

    urlsWithIssues = []

    for url in playlist:
        try:
            download(url)
        except Exception as e:
            urlsWithIssues.append(url)
            print("erreur {}".format(e))

    print("URLS dont le téléchargement a jeté une erreur : {}".format(urlsWithIssues))

from pytube import YouTube
from bs4 import BeautifulSoup

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_in_file(filename):
    f = open(filename, 'r')
    soup = BeautifulSoup(f.read(), 'html.parser')
    f.close()
    return soup

def read_favoris():
    listUrl = []
    soup = read_in_file('favoris.html')
    for line in soup.find_all('a'):
        url = line.get('href').replace("https", "http")
        listUrl.append(url)
    return listUrl

def read_txt():
    listUrl = []
    lines = open("ToDL.txt", 'r').read().split('\n')
    for line in lines:
        url = line.replace("https", "http")
        listUrl.append(url)
    return listUrl
def download(link):
    # link = "http://www.youtube.com/watch?v=nsm4ReJaED0&ab_channel=CTanganaVEVO"
    yt = YouTube(link)

    # Showing details
    # Getting the audio
    audio = yt.streams.get_audio_only()

    title_corrected = yt.title # TODO
    title_corrected = "Who Are You Really"

    author_corrected = yt.author # TODO
    author_corrected = "Mikky Ekko"

    filename = author_corrected+" - "+title_corrected+".mp3"
    audio.download(output_path="Musiques_DL", filename=filename, max_retries=3)
    print("Download completed : "+yt.title)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    listeUrlsWithProblem = []

    # listeUrls = read_favoris()
    # listeUrls = read_txt()
    #
    # for url in listeUrls:
    #     try:
    #         download(url)
    #     except :
    #         listeUrlsWithProblem.append(url)
    #         print("erreur")
    #
    # print(listeUrlsWithProblem)

    download("https://www.youtube.com/watch?v=Jk1dkG8IK10&ab_channel=00laurenrebeccah")

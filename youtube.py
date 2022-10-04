from pytube import YouTube
link = input("Укажите ссылку на видео:")
yt = YouTube(link)
yt.streams.filter(progressive=True)
# print(yt.streams)
print(yt.title)
type = input("Выберите тип скачивания 1-Видео+аудио, 2 - Только аудио: ")
if type == "1":
    stream = yt.streams.get_by_itag(22)
else:
    stream = yt.streams.get_by_itag(140)
stream.download()

def rick():
    yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    yt.streams.filter(progressive=True)
    stream = yt.streams.get_by_itag(17)
    stream.download()   
rick() # :)
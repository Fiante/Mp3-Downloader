from pytube import YouTube
import os


link = input("Videonun linkini buraya giriniz:")
directory = input("İndirilen videonun adının ne olmasını istersiniz? ")

try:
    yt = YouTube(link)
except:
    print("Videon bulunamadı. Linki kontrol ediniz.")
    exit()

mp3 = yt.streams.filter(only_audio=True).first()

print("İndiriliyor...")

output = mp3.download(directory)

base, ext = os.path.splitext(output)
to_mp3 = base + ".mp3"
os.rename(output, to_mp3)

print("İndirme Tamamlandı")

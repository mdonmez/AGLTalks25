from audio_downloader import AudioDownloader
import json

with open("music-data.json", "r") as f:
    data = json.load(f)

downloader = AudioDownloader()
# lets go through the data and download the audio heres the data
# [{"name":"hatice_hilal_aslan","url":"https://music.youtube.com/watch?v=wjNln9mXuTI","title":"Deceptacon","start":1.38,"end":2.01},{"name":"betul_aydog","url":"https://music.youtube.com/watch?v=4KLVnmChtIE","title":"Boys Don't Cry","start":0.00,"end":0.22},{"name":"yasin_efe_baser","url":"https://music.youtube.com/watch?v=oaDnuExc1sI","title":"This Cocaine Makes Me Feel Like I'm On This Song","start":0.00,"end":0.25},{"name":"elif_barin","url":"https://music.youtube.com/watch?v=6LEs1yKXnb8","title":"Tek It","start":0.00,"end":0.17},{"name":"hacer_bayram","url":"https://music.youtube.com/watch?v=llmbcMmZuQ4","title":"Brother Louie Mix '98 (Radio Edit) (feat. Eric Singleton)","start":0.00,"end":0.17},{"name":"ezgi_karaaslan","url":"https://music.youtube.com/watch?v=n-IwmbARwBo","title":"Can I Call You Tonight?","start":1.10,"end":1.32},{"name":"nehir_ogunday","url":"https://music.youtube.com/watch?v=gG9fEaITgCk","title":"Age of Consent","start":1.38,"end":1.50}]


output_folder = "musics"

# go through name, url, start, end and download the audio
for item in data:
    name = item["name"]
    url = item["url"]
    start = item["start"]
    end = item["end"]
    downloader.download_and_process_audio(
        url, start, end, 1000, 0000, f"{output_folder}/{name}.wav"
    )

import os
import yt_dlp
from pydub import AudioSegment


class AudioDownloader:
    def __init__(self):
        pass

    def download_and_process_audio(
        self, url, start_time, end_time, fade_in, fade_out, output_location
    ):
        """
        Downloads audio from a URL, trims it, applies fade in/out, and exports to output_location.
        Args:
            url (str): Source video/audio URL
            start_time (str): Start time in 'mm:ss' format
            end_time (str): End time in 'mm:ss' format
            fade_in (int): Fade-in duration in milliseconds
            fade_out (int): Fade-out duration in milliseconds
            output_location (str): Output file path (e.g. 'output.wav')
        """
        temp_file_base = "temp_audio"
        temp_file_downloaded = temp_file_base + "_dl.m4a"

        def time_str_to_ms(time_str):
            minutes, seconds = map(int, time_str.strip().split(":"))
            return (minutes * 60 + seconds) * 1000

        start_ms = time_str_to_ms(start_time)
        end_ms = time_str_to_ms(end_time)
        if end_ms <= start_ms:
            raise ValueError("End time must be greater than start time.")

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": temp_file_base + "_dl",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "m4a",
                    "preferredquality": "0",
                }
            ],
        }

        print("Downloading full audio in best quality (m4a)...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Trimming and applying fade-in/fade-out...")
        audio = AudioSegment.from_file(temp_file_downloaded)
        segment = audio[start_ms:end_ms]
        # Apply fades only if duration is greater than 0
        if fade_in and fade_in > 0:
            segment = segment.fade_in(fade_in)
        if fade_out and fade_out > 0:
            segment = segment.fade_out(fade_out)

        # Output format and codec based on extension
        ext = os.path.splitext(output_location)[1].lower()
        if ext == ".wav":
            output_audio_format = "wav"
            output_audio_codec = "pcm_s16le"
        elif ext == ".flac":
            output_audio_format = "flac"
            output_audio_codec = "flac"
        else:
            raise ValueError("Unsupported output file format. Use .wav or .flac.")

        segment.export(
            output_location, format=output_audio_format, codec=output_audio_codec
        )
        os.remove(temp_file_downloaded)
        print(f"Done! Exported to: {output_location}")


with open("music_data.json", "r") as f:
    data = json.load(f)

downloader = AudioDownloader()

output_folder = "downloaded_musics"

# go through name, url, start, end and download the audio
for item in data:
    name = item["name"]
    url = item["url"]
    start = item["start"]
    end = item["end"]
    downloader.download_and_process_audio(
        url, start, end, 1000, 3000, f"{output_folder}/{name}.wav"
    )

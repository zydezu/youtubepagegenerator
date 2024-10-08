import subprocess
import os, sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

os.system("")


os.system("title " + "Downloading.......")


input()






class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'

if 'yt-dlp' not in installed_packages and 'rangehttpserver' not in installed_packages:
    print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
    print(f"{bcolors.OKBLUE}Installing packages...")
    print(f"{bcolors.LINE}---------------------------------------")
    subprocess.run('pip install -r requirements.txt', shell=True)
    print(f"{bcolors.LINE}---------------------------------------")

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

# Define the command
command = [
    'yt-dlp', '--skip-download',
    'https://www.youtube.com/watch?v=jOrPYP-HZIY',
    '--print', '%(title)s'
]

# os.system('yt-dlp --skip-download https://www.youtube.com/watch?v=jOrPYP-HZIY --print "%(title)s"')

# output = subprocess.check_output(command, shell=True, text=True).replace('\n', '')
# print(output)

# with open('TEST.txt', 'w', encoding="utf-8") as file:
#     file.write(output)

ytdlp_opts = {
    "skip_download": True,
    'quiet': True
}

with YoutubeDL(ytdlp_opts) as ytdlp:
    info_dict = ytdlp.extract_info("https://www.youtube.com/watch?v=jOrPYP-HZIY", download=False)
    videoid = info_dict.get('id', None)
    videotitle = info_dict.get('title', None)

print(videoid + '\n' + videotitle)

ytdlp_opts = {
    'format': 'bestvideo+bestaudio/best',
    'postprocessors': [
        {
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }
    ],
    'writeinfojson': True,  # Ensure info.json is written, which contains comments
    'getcomments': True,
    'outtmpl': f'TEST/{videoid}/videos/%(title)s.%(ext)s',
}
while True:
    try:
        with YoutubeDL(ytdlp_opts) as ytdlp:
            ytdlp.download("https://www.youtube.com/watch?v=jOrPYP-HZIY")
        break
    except:
        print("Error! Retrying download...")
import subprocess
import os, sys
from os import walk

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

os.system("")

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

ytdlp_opts = {
    "skip_download": True,
    'quiet': True
}

with YoutubeDL(ytdlp_opts) as ytdlp:
    info_dict = ytdlp.extract_info("https://www.youtube.com/watch?v=jOrPYP-HZIY", download=False)
    videoid = info_dict.get('id', None)
    videotitle = info_dict.get('title', None)

print(videoid + '\n' + videotitle)

# videoIDs = next(os.walk(os.path.join(os.getcwd(), "generated")))[1]
videoIDs = next(os.walk(os.path.join(os.getcwd(), "TEST")))[1]
for video in videoIDs:
    print(video)
    filenames = next(walk(os.path.join(os.getcwd(), "TEST", video, "videos"), (None, None, [])))[2] # [] if no file
    filetorename = ""
    for file in filenames:
        if '.info.json' in file:
            infofilepath = os.path.join(os.getcwd(), "TEST", video, "videos", file)
            unixtime = os.path.getmtime(os.path.join(infofilepath))
            os.rename(os.path.join(infofilepath), 
                      os.path.join(infofilepath.replace('.info.json', f'.info.json.old{unixtime}')))

ytdlp_opts = {
    "skip_download": True,
    'quiet': True,
    'writeinfojson': True, # Ensure info.json is written, which contains comments
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
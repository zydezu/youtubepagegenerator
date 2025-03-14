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
    os.system("title " + "Installing packages...")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
    print(f"{bcolors.OKBLUE}Installing packages...")
    print(f"{bcolors.LINE}---------------------------------------")
    subprocess.run('pip install -r requirements.txt', shell=True)
    print(f"{bcolors.LINE}---------------------------------------")

from yt_dlp import YoutubeDL

videoIDs = next(os.walk(os.path.join(os.getcwd(), "generated")))[1]
i = 0
for videoID in videoIDs:
    i+=1
    filenames = next(walk(os.path.join(os.getcwd(), "generated", videoID, "videos"), (None, None, [])))[2] # [] if no file
    filetorename = ""
    for file in filenames:
        if '.info.json' in file:
            # Rename the old info.json file
            infofilepath = os.path.join(os.getcwd(), "generated", videoID, "videos", file)
            unixtime = os.path.getmtime(os.path.join(infofilepath))
            os.rename(os.path.join(infofilepath), 
                      os.path.join(infofilepath.replace('.info.json', f'.info.json.old{unixtime}')))

            print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
            print(f"{bcolors.OKBLUE}Updating '{file.replace('.info.json', '')}' [{videoID}] - {i}/{len(videoIDs)}...{bcolors.ENDC}")
            os.system("title " + f"Updating '{file.replace('.info.json', '')}' [{videoID}] - {i}/{len(videoIDs)}...")
            ytdlp_opts = {
                "skip_download": True,
                'restrictfilenames': True,
                'writeinfojson': True, # Ensure info.json is written, which contains comments
                'getcomments': True,
                'outtmpl': {
                    'default': f'generated/{videoID}/videos/video.%(ext)s',
                    'infojson': f'generated/{videoID}/videos/video',
                    'thumbnail': f'generated/{videoID}/videos/video.%(ext)s',
                },
            }
            while True:
                try:
                    with YoutubeDL(ytdlp_opts) as ytdlp:
                        ytdlp.download(f"https://www.youtube.com/watch?v={videoID}")
                    break
                except:
                    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
                    print(f"{bcolors.WARNING}Error! Couldn't download...")
                    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
                    break
            break

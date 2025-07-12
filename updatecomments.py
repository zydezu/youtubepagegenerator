import os
from os import walk
from yt_dlp import YoutubeDL

os.system("")

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'

def set_terminal_title(title):
    if os.name == 'nt':  # Windows
        os.system(f"title {title}")
    else:  # Unix/Linux/Mac
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

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
            set_terminal_title(f"Updating '{file.replace('.info.json', '')}' [{videoID}] - {i}/{len(videoIDs)}...")
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

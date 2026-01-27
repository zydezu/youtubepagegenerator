import os
import downloadvideo
import runserver

os.system("")
class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'

videoid = downloadvideo.startvideodownload()
runserver.startserver(url=f"http://localhost:9999/generated/{videoid}/")
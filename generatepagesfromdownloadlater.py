import os
import downloadvideo

DOWNLOADLATERFILE = 'downloadlater.txt'

os.system("")

with open(DOWNLOADLATERFILE, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

total = len(urls)
for index, url in enumerate(urls):
    print(f"{downloadvideo.bcolors.LINE}---------------------------------------{downloadvideo.bcolors.WARNING}")
    print(f"{downloadvideo.bcolors.OKBLUE}Downloading video {index + 1} / {total}...")
    print(f"{downloadvideo.bcolors.LINE}---------------------------------------{downloadvideo.bcolors.ENDC}")
    downloadvideo.startvideodownload(url, f"| ({index + 1} / {total})")

with open(DOWNLOADLATERFILE, 'w') as file:
    pass
import os
import downloadvideo

DOWNLOADLATERFILE = '.downloadlater.txt'

os.system("")

with open(DOWNLOADLATERFILE, 'r') as file:
    urls = file.readlines()

for index, url in enumerate(urls):
    print(f"{downloadvideo.bcolors.LINE}---------------------------------------{downloadvideo.bcolors.WARNING}")
    print(f"{downloadvideo.bcolors.OKBLUE}Downloading video {index + 1} / {len(urls)}...")
    print(f"{downloadvideo.bcolors.LINE}---------------------------------------{downloadvideo.bcolors.ENDC}")
    downloadvideo.startvideodownload(url.strip(), f"| ({index + 1} / {len(urls)})")
    
    # Remove the downloaded URL from the file
    with open(DOWNLOADLATERFILE, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(DOWNLOADLATERFILE, 'w') as fout:
        fout.writelines(data[1:])
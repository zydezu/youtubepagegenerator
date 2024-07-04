import subprocess, os
from datetime import datetime

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'

def startvideodownload():
    print(f"{bcolors.OKBLUE}Enter the link of the {bcolors.WARNING}video{bcolors.OKBLUE} to generate a page for...{bcolors.ENDC}")
    print(f"{bcolors.LINE}---------------------------------------")
    link = input(f"{bcolors.WARNING}Link {bcolors.ENDC}> {bcolors.WARNING}")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
    print(f"{bcolors.OKBLUE}Downloading video...")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    videoid = subprocess.check_output('yt-dlp --skip-download {0} --print "%(id)s"'.format(link), shell=True).decode('utf-8').replace('\n', '')
    videotitle = subprocess.check_output('yt-dlp --skip-download {0} --print "%(title)s"'.format(link), shell=True).decode('windows-1252').replace('\n', '')
    quality = """ -f bestvideo+bestaudio --remux mp4 """
    command = "yt-dlp" + quality + link + " --restrict-filenames --add-metadata --embed-subs --write-subs --write-auto-subs --write-comments --write-thumbnail -P generated/{0}/videos".format(videoid)
    subprocess.run(command, shell=True)

    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Generating page...")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

    def basestring(lst):
        if not lst:
            return ""
        common_sub = lst[0]
        for string in lst[1:]:
            common_sub = ''.join(c1 for c1, c2 in zip(common_sub, string) if c1 == c2)
            if not common_sub:
                break
        return common_sub

    fileslist = os.listdir('generated/{0}/videos'.format(videoid))
    base = basestring(fileslist)[:-1]
    filename = base + '.mp4'
    imagepath = base + '.webp'

    with open('template.txt', 'r') as file:
        templatefile = file.read()
        outputfile = templatefile.format(videotitle=videotitle, filename=filename, icon=imagepath)
        with open("generated/{0}/index.html".format(videoid), "w") as writefile:
            writefile.writelines(outputfile)

    allLines = []
    with open('listofvideos.txt', 'a') as file:
        file.write("""\t{0} | <a href="generated/{1}/">generated/{1}/</a> | {2}<br/>\n""".format(videotitle, videoid, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    with open('listofvideos.txt', 'r') as file:
        allLines = file.readlines()

    with open('index.html', 'w') as file:
        file.writelines("""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Archived Videos</title>
        <link rel="stylesheet" href="style.css">
        <style>body{{margin:15px;}}</style>
    </head>
    <body>
    {0}
    </body>
    </html>""".format("".join(allLines)))

    print("File written to index.html!")

    return videoid
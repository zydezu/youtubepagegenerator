import subprocess, os
import sys
import webbrowser

os.system("")
class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

# use rangehttpserver as it supports range headers (fixes video scrubbing in the browser)
if 'rangehttpserver' not in installed_packages:
    print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
    print(f"{bcolors.OKBLUE}Installing packages...")
    print(f"{bcolors.LINE}---------------------------------------")
    subprocess.run('pip install -r requirements.txt')
    print(f"{bcolors.LINE}---------------------------------------")

print(f"{bcolors.OKBLUE}Enter the link of the {bcolors.WARNING}video{bcolors.OKBLUE} to generate a page for...{bcolors.ENDC}")
print(f"{bcolors.LINE}---------------------------------------")
link = input(f"{bcolors.WARNING}Link {bcolors.ENDC}> {bcolors.WARNING}")
print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
print(f"{bcolors.OKBLUE}Downloading video...")
print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
videoid = subprocess.check_output('yt-dlp --skip-download {0} --print %(id)s'.format(link)).decode('utf-8').replace('\n', '')
videotitle = subprocess.check_output('yt-dlp --skip-download {0} --print %(title)s'.format(link)).decode('utf-8').replace('\n', '')
quality = """ -f bestvideo+bestaudio --remux mp4 """
command = "yt-dlp" + quality + link + " --restrict-filenames --add-metadata --embed-subs --write-subs --write-comments --write-thumbnail -P generated/{0}/videos".format(videoid)
subprocess.run(command)

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

print("File written to index.html!")

print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Starting web server and opening page...")
print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

# make a localhost web server and open generated index.html, since CORS blocks file:// fetching
webbrowser.open('http://localhost:8000/generated/{0}/'.format(videoid))
subprocess.run('python -m RangeHTTPServer')
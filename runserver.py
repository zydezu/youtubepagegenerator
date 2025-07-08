import subprocess, os
import sys
import webbrowser
import time

os.system("")
class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'

def startserver(url="http://localhost:8000/index.html"):
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Starting web server and opening page...")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

    # make a localhost web server and open generated index.html, since CORS blocks file:// fetching
    os.system("title " + "Running web server...")
    subprocess.Popen(['python', '-m', 'RangeHTTPServer'])
    time.sleep(3)
    webbrowser.open(url)

startserver()
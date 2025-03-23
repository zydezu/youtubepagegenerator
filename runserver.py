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

    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    # use rangehttpserver as it supports range headers (fixes video scrubbing in the browser)
    if 'rangehttpserver' not in installed_packages:
        os.system("title " + "Installing packages...")
        print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
        print(f"{bcolors.OKBLUE}Installing packages...")
        print(f"{bcolors.LINE}---------------------------------------")
        subprocess.run('pip install -r requirements.txt', shell=True)
        print(f"{bcolors.LINE}---------------------------------------")


    # make a localhost web server and open generated index.html, since CORS blocks file:// fetching
    os.system("title " + "Running web server...")
    subprocess.Popen(['python', '-m', 'RangeHTTPServer'])
    webbrowser.open(url)

startserver()
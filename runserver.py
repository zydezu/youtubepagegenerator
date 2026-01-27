import subprocess, os, sys, webbrowser

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

def startserver(url="http://localhost:9999/index.html"):
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Starting web server and opening page...")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

    # make a localhost web server and open generated index.html, since CORS blocks file:// fetching
    set_terminal_title("Running web server...")
    subprocess.Popen(['python', '-m', 'RangeHTTPServer', '9999'])
    webbrowser.open(url)

if __name__ == "__main__":
    startserver()
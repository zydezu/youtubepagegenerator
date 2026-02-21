import subprocess, os, sys, webbrowser

os.system("")

VENV_PYTHON = os.path.join(os.path.dirname(__file__), ".venv", "bin", "python")
PORT = "3099"

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

def startserver(url=f"http://localhost:{PORT}/index.html"):
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Starting web server and opening page...")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

    # make a localhost web server and open generated index.html, since CORS blocks file:// fetching
    set_terminal_title("Running web server...")
    subprocess.Popen([VENV_PYTHON, '-m', 'RangeHTTPServer', PORT])
    webbrowser.open(url)

if __name__ == "__main__":
    startserver()
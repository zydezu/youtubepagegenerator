import subprocess, os, sys, webbrowser, time, socket

os.system("")

VENV_PYTHON = os.path.join(os.path.dirname(__file__), ".venv", "bin", "python")
START_PORT = 3099

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'

def set_terminal_title(title):
    if os.name == 'nt':
        os.system(f"title {title}")
    else:
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

def find_free_port(start_port):
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    return start_port

def startserver(path="/index.html"):
    port = find_free_port(START_PORT)
    url = f"http://localhost:{port}{path}"
    
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Starting web server on port {port}...")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

    set_terminal_title(f"Running web server on port {port}...")
    server_proc = subprocess.Popen([VENV_PYTHON, '-m', 'RangeHTTPServer', str(port)])
    
    webbrowser.open(url)
    time.sleep(1)
    
    try:
        while True:
            time.sleep(2)
            if os.name == 'nt':
                result = subprocess.run(['tasklist'], capture_output=True, text=True)
                if 'chrome' not in result.stdout.lower() and 'firefox' not in result.stdout.lower():
                    break
            else:
                result = subprocess.run(['pgrep', '-f', 'chrome|firefox|brave|edge'], capture_output=True)
                if result.returncode != 0:
                    break
    except KeyboardInterrupt:
        pass
    finally:
        server_proc.terminate()
        server_proc.wait()
        print(f"\n{bcolors.WARNING}Server stopped.{bcolors.ENDC}")


if __name__ == "__main__":
    startserver()
import os, sys, http.server, ssl, threading, webbrowser, time

os.system("")

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

def run_https_server(port=9999, cert='cert.pem', key='key.pem'):
    handler = http.server.SimpleHTTPRequestHandler
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, handler)

    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=cert, keyfile=key)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

        print(f"{bcolors.OKBLUE}Serving on https://localhost:{port}{bcolors.ENDC}")
        httpd.serve_forever()
    except Exception as e:
        print(f"{bcolors.WARNING}Failed to start server: {e}{bcolors.ENDC}")

def startserver(url="https://localhost:9999/index.html"):
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Starting HTTPS web server and opening page...{bcolors.ENDC}")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

    set_terminal_title("Running HTTPS web server...")

    thread = threading.Thread(target=run_https_server)
    thread.start()

    # Wait a moment to let server start
    time.sleep(1.5)

    webbrowser.open(url)

if __name__ == "__main__":
    startserver()
    input("Press Enter to quit...\n")
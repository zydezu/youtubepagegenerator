import os, sys, http.server, ssl, threading, webbrowser

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

def run_https_server(port=9999, cert='cert.pem', key='key.pem'):
    handler = http.server.SimpleHTTPRequestHandler
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, handler)

    # Use SSLContext instead of deprecated wrap_socket
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert, keyfile=key)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"{bcolors.OKBLUE}Serving on https://localhost:{port}{bcolors.ENDC}")
    httpd.serve_forever()

def startserver(url="https://localhost:9999/index.html"):
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Starting HTTPS web server and opening page...{bcolors.ENDC}")
    print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")

    set_terminal_title("Running HTTPS web server...")

    # Run the server in a thread so we can open the browser without blocking
    thread = threading.Thread(target=run_https_server)
    thread.start()

    # Open the web page
    webbrowser.open(url)

if __name__ == "__main__":
    startserver()
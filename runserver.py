import subprocess
import webbrowser

# make a localhost web server and open generated index.html, since CORS blocks file:// fetching
webbrowser.open('http://localhost:8000/index.html')
subprocess.run('python -m RangeHTTPServer')
import subprocess
import os

# Define the command
command = [
    'yt-dlp', '--skip-download',
    'https://www.youtube.com/watch?v=jOrPYP-HZIY',
    '--print', '%(title)s'
]

# os.system('yt-dlp --skip-download https://www.youtube.com/watch?v=jOrPYP-HZIY --print "%(title)s"')
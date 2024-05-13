# youtubepagegenerator

Generates a HTML page for a YouTube video with a provided link via Python.

## Requirements

- Python
- yt-dlp (on path) or via included yt-dlp.exe

## Usage

Run `generatepage.py`  and paste in the link of the desired video. Designed specifically for YouTube videos, results from other sites may vary.

Outputted pages will be in `generated/[videoID]/`, pages will open automatically in your browser via `
http://localhost:8000/...`

Alternatively, run `runserver.py` to open a page with a list of archived videos

## Changelog

### 2024-05-13

- Fixed downloading comments with a different build of yt-dlp.exe
- Changed css and scripts
- Added an `index.html` with all archived videos listed

### 2024-04-07

- Included a yt-dlp.exe for new users
- Packages are now checked instead of always attempting to install from `requirements.txt`

## To Do

- Download subtitles and convert them to WEBVTT automatically
- More YouTube like interface (choose css - new - old?), refering to the internet checkpoints page <https://internetcheckpoint.page/Q9XTqQbuavI>

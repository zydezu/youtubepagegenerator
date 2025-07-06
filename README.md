# youtubepagegenerator

Generates a HTML page for a YouTube video with a provided link via Python.

## Requirements

- Python

## Usage

Run `generatepage.py`  and paste in the link of the desired video. Designed specifically for YouTube videos, results from other sites may vary.

Outputted pages will be in `generated/[videoID]/`, pages will usually open in browser at `http://localhost:8000/...`.

Alternatively, run `runserver.py` to open a page with a list of archived videos.

There are also other scripts that perform different functions.

## Changelog

### 2025-03-23

- ADD: update video entries in `.downloadlater.txt`, `index.html`, and `listofvideos.txt`, refresh video links

### 2025-03-18

- ADD: implement video download functionality from a list, refactor download handling in `downloadvideo.py`

### 2025-02-28

- ADD: include new video entries in `index.html` and `listofvideos.txt`, update `runserver.py` to start server automatically

### 2025-02-26

- REFACTOR: update video download and server handling; rename old info.json files

### 2025-02-18

- Improve script loading when offline

### 2024-10-10

- Ambient mode is now OFF by default
- Automatically disable ambient mode when frame drops occur
- Added `updatecomments.py` which updates comment json files

### 2024-10-08

- Add window title changing

### 2024-08-03

- Redo code to improve response times

### 2024-07-07

- Fix unicode errors (hopefully once and for all...)
- Code now uses the yt-dlp python package

### 2024-07-03

- Fix for unix

### 2024-06-23

- Reduce code redundancy
- Write automatic subtitles

### 2024-05-13

- Fixed downloading comments with a different build of yt-dlp.exe
- Changed css and scripts
- Added an `index.html` with all archived videos listed
- Fix 4:3 videos

### 2024-04-07

- Included a yt-dlp.exe for new users
- Packages are now checked instead of always attempting to install from `requirements.txt`

## To Do

- Download subtitles and convert them to WEBVTT automatically
- More YouTube like interface (choose css - new - old?), refering to the internet checkpoints page <https://internetcheckpoint.page/Q9XTqQbuavI>

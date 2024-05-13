# youtubepagegenerator

Generates a HTML page for a YouTube video with a provided link via Python.

## Requirements

- Python
- yt-dlp (on path) or via included yt-dlp.exe

## Usage

Run `generatepage.py`  and paste in the link of the desired video. Designed specifically for YouTube videos, results from other sites may vary.

Outputted pages will be in `generated/[videoID]/`, pages will open automatically in your browser via `localhost`

## Changelog

### 2024-04-07

- Included a yt-dlp.exe for new users
- Packages are now checked instead of always attempting to install from `requirements.txt`

## To Do

- Download subtitles and convert them to WEBVTT automatically
- Wait for yt-dlp to fix comments downloading
- More YouTube like interface (choose css - new - old?), refering to the internet checkpoints page <https://internetcheckpoint.page/Q9XTqQbuavI>

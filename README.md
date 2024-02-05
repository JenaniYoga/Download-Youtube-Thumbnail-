# Download YouTube Thumbnail
This Python script allows you to easily download the thumbnail of a YouTube video by providing its URL.

## Usage
1. Make sure you have Python installed on your system.
2. Install the `wget` library if you haven't already installed it. You can install it using pip:
   pip install wget

3. Run the script by executing the `Download_Youtube_Thumbnail.py` file.
4. Enter the URL of the YouTube video when prompted.
5. The script will download the thumbnail and save it in the current directory.

## Instructions
- When you run the script, it prompts you to enter the URL of the YouTube video.
- It extracts the video ID from the URL and constructs the URL of the thumbnail image.
- The script then downloads the thumbnail using the `wget` library.
- Once downloaded, the script notifies you that the download is complete.

## Note
- The thumbnail is saved as `maxresdefault.jpg` in the current directory.
- Ensure that you have proper permissions to write files in the current directory.
- This script is intended for personal and educational use only.

## Requirements
- Python 3.x
- wget library

## Disclaimer
This script is provided as is without any guarantees. Use it at your own risk. The developer is not responsible for any misuse or damage caused by this script.


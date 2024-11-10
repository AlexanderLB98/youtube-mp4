import os
import sys

import yt_dlp


def download_video(url):
    # Define the output path in the ~/videos directory
    output_path = os.path.expanduser("~/videos/video_twitter.mp4")

    # yt-dlp configuration options
    ydl_opts = {"format": "best", "outtmpl": output_path}  # Save to ~/videos

    try:
        # Create the ~/videos directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download complete. Video saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Check if a URL was passed as an argument
if len(sys.argv) > 1:
    url = sys.argv[1]
    download_video(url)
else:
    print("Please provide the Twitter (X) video URL.")
    print("Usage: python download_video.py <URL>")

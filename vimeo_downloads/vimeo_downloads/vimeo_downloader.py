import subprocess
import os

def download_vimeo_video(video_url, password, output_path="."):
    """
    Downloads a password-protected Vimeo video using yt-dlp.

    Args:
        video_url (str): The URL of the Vimeo video.
        password (str): The password for the video.
        output_path (str, optional): The directory to save the video in. Defaults to ".".
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    command = [
        'yt-dlp',
        '--cookies-from-browser', 'firefox',
        '--video-password', password,
        '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
        video_url
    ]

    try:
        print(f"Downloading video from: {video_url}")
        subprocess.run(command, check=True)
        print("Download completed successfully!")
    except FileNotFoundError:
        print("Error: 'yt-dlp' command not found.")
        print("Please make sure you have yt-dlp installed and in your system's PATH.")
        print("You can install it by running: pip install yt-dlp")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during download: {e}")

if __name__ == '__main__':
    # --- Video Information ---
    VIMEO_URL = "https://vimeo.com/1104553657"
    VIMEO_PASSWORD = "0726071225"
    DOWNLOAD_DIRECTORY = "vimeo_downloads"
    # -------------------------

    download_vimeo_video(VIMEO_URL, VIMEO_PASSWORD, DOWNLOAD_DIRECTORY)
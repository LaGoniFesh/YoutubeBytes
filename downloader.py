#This was made in Python3 to Download Mass YouTube Videos And Playlist/Mixes


import yt_dlp

def download_video(url):
    try:
        print("[+] Downloading with yt-dlp...")
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("[+] Download complete!")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    # Known-safe YouTube URL
    video_url = "https://www.youtube.com/watch?v=rwhtH0b7KRY"
    #Replace the above youtube url with any video or playlist you would like.
    download_video(video_url)

import os
import yt_dlp

def download_youtube_video():
    # Exact path to your ffmpeg.exe
    ffmpeg_path = r"C:\Users\Windows 10\Desktop\YouTube PlayList Downloader\ffmpeg\bin\ffmpeg.exe" #users will need to Change this
    
    # Ask for video URL
    video_url = input("Enter YouTube Video URL: ").strip()
    if not video_url:
        print("No URL provided. Exiting.")
        return
    
    # EXTRACT ONLY THE VIDEO PART - THIS IS THE KEY FIX!
    # Remove playlist parameters to force single video download
    if "&list=" in video_url:
        video_url = video_url.split("&list=")[0]
    if "&index=" in video_url:
        video_url = video_url.split("&index=")[0]
    
    # Ask for download folder path
    download_folder = input("Enter download folder path (e.g., C:/Users/YourName/Videos): ").strip()
    if not download_folder:
        print("No folder provided. Exiting.")
        return
    
    # Replace backslashes with forward slashes
    download_folder = download_folder.replace('\\', '/')
    
    # Quality selection
    print("\nSelect video quality:")
    print("1. Best available (4K/1440p/1080p)")
    print("2. 1440p QHD")
    print("3. 1080p Full HD")
    print("4. 720p HD")
    print("5. 480p")
    print("6. 360p")
    print("7. Audio only (MP3)")
    
    quality_choice = input("Enter choice (1-7, default=1): ").strip() or "1"
    
    # Map choices to format strings
    quality_map = {
        "1": "bestvideo+bestaudio/best",
        "2": "bestvideo[height<=1440]+bestaudio/best",
        "3": "bestvideo[height<=1080]+bestaudio/best",
        "4": "bestvideo[height<=720]+bestaudio/best",
        "5": "best[height<=480]",
        "6": "best[height<=360]",
        "7": "bestaudio/best",
    }
    
    format_selection = quality_map.get(quality_choice, "bestvideo+bestaudio/best")
    
    if not os.path.exists(download_folder):
        print("Folder does not exist. Creating it...")
        os.makedirs(download_folder, exist_ok=True)
    
    try:
        # Set up yt-dlp options with FFmpeg path
        ydl_opts = {
            'ffmpeg_location': ffmpeg_path,
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'format': format_selection,
            'merge_output_format': 'mp4',
            'quiet': False,
            'no_warnings': False,
            'progress_hooks': [progress_hook],
            'ignoreerrors': True,
            # ADD THIS TO FORCE SINGLE VIDEO (NOT PLAYLIST)
            'noplaylist': True,
        }
        
        # For audio only
        if quality_choice == "7":
            ydl_opts.update({
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            })
        
        print("\nStarting SINGLE video download...")
        print(f"Processing URL: {video_url}")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract info first to get video title
            info = ydl.extract_info(video_url, download=False)
            video_title = info.get('title', 'Video')
            
            print(f"Video: {video_title}")
            print(f"Quality: {get_quality_name(quality_choice)}")
            
            # Now download single video
            ydl.download([video_url])
            
        print(f"\n✅ Single video download completed!")
        print(f"📁 File saved to: {download_folder}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def get_quality_name(choice):
    """Get human-readable quality name"""
    qualities = {
        "1": "Best available (4K/1440p/1080p)",
        "2": "1440p QHD", 
        "3": "1080p Full HD",
        "4": "720p HD",
        "5": "480p",
        "6": "360p",
        "7": "Audio only (MP3)"
    }
    return qualities.get(choice, "Best available")

def progress_hook(d):
    if d['status'] == 'downloading':
        filename = os.path.basename(d.get('filename', 'Unknown'))
        print(f"Downloading: {filename} - {d.get('_percent_str', '0%')} complete")
    elif d['status'] == 'finished':
        filename = os.path.basename(d.get('filename', 'Unknown'))
        print(f"✓ Finished: {filename}")

if __name__ == "__main__":
    download_youtube_video()
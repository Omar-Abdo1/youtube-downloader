YouTube Video & Playlist Downloader
A powerful Python-based tool for downloading YouTube videos and playlists with customizable quality options. This tool automatically handles video and audio merging for high-quality downloads.

🚀 Features
Download Entire Playlists - Automatically organizes videos into playlist folders

Download Single Videos - Works even with playlist URLs containing &list= parameters

Multiple Quality Options - Choose from 360p to 4K quality

Automatic Merging - FFmpeg integration for perfect video+audio synchronization

Progress Tracking - Real-time download progress display

Error Handling - Continues downloads even if some videos fail

Cross-Platform - Works on Windows, macOS, and Linux

📋 Prerequisites
Before using this tool, ensure you have:

Python 3.6 or higher - Download Python

During installation, check "Add Python to PATH"

FFmpeg (required for high-quality video merging) - Download FFmpeg

🔧 Installation
1. Download the Tool
Download and extract the ZIP file from GitHub, or clone the repository:

bash
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
2. Install Python Dependencies
bash
pip install -r requirements.txt
3. Install FFmpeg (Required for High Quality)
Windows Installation:
Download FFmpeg from https://www.gyan.dev/ffmpeg/builds/

Download ffmpeg-release-full.7z

Extract to C:\ffmpeg\

Add to PATH:

Press Windows + S, type "environment variables"

Click "Edit the system environment variables"

Click "Environment Variables"

Under "System variables", find "Path" and click "Edit"

Click "New" and add: C:\ffmpeg\bin

Click OK → OK → OK

Verify FFmpeg Installation:
bash
ffmpeg -version
🎯 Usage
Download a Playlist
bash
python youtube_playlist_downloader.py
Enter the playlist URL (e.g., https://www.youtube.com/playlist?list=YOUR_LIST_ID)

Choose download folder location

Select video quality (1-7)

Download a Single Video
bash
python youtube_video_downloader.py
Enter any YouTube video URL (even with &list= parameters)

Choose download folder location

Select video quality (1-7)

⚙️ Quality Options
When prompted, choose from:

Best available (4K/1440p/1080p) - Highest quality available

1440p QHD - 2560×1440 resolution

1080p Full HD - 1920×1080 resolution

720p HD - 1280×720 resolution (Recommended balance)

480p - Standard definition

360p - Low quality (small file size)

Audio only - MP3 audio only (192kbps)

📁 Output Structure
text
Your-Download-Folder/
├── Playlist Name 1/
│   ├── Video Title 1.mp4
│   ├── Video Title 2.mp4
│   └── ...
└── Individual Videos/
    ├── Single Video Title 1.mp4
    └── Single Video Title 2.mp4
🔍 Troubleshooting
Common Issues & Solutions:
1. "FFmpeg not found" error

Solution: Install FFmpeg and add to PATH, or place ffmpeg.exe in the script folder

2. "HTTP Error 400: Bad Request"

Solution: Update yt-dlp: pip install --upgrade yt-dlp

3. Videos download as separate files

Solution: Ensure FFmpeg is properly installed for merging

4. "Module not found" errors

Solution: Install requirements: pip install -r requirements.txt

5. Download stops or fails

Solution: The script will automatically retry failed downloads

Need Help?
Create an issue on GitHub with:

The exact error message

Steps to reproduce the issue

Your operating system and Python version

📝 File Structure
text
youtube-downloader/
├── youtube_playlist_downloader.py  # Main playlist download script
├── youtube_video_downloader.py     # Single video download script
├── requirements.txt                # Python dependencies
├── README.md                       # This documentation
└── ffmpeg/                         # FFmpeg binaries (optional)
    └── bin/
        ├── ffmpeg.exe
        ├── ffplay.exe
        └── ffprobe.exe
⚠️ Legal Disclaimer
This tool is intended for personal use only. Please:

Respect copyright laws in your country

Follow YouTube's Terms of Service

Only download content you have rights to access

The developers are not responsible for misuse of this tool

🤝 Contributing
Contributions are welcome! Feel free to:

Report bugs and issues

Suggest new features

Submit pull requests

Improve documentation

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🆓 Free and Open Source
This is a free, open-source tool maintained by the community. If you find it useful, please give it a star on GitHub! ⭐

Happy Downloading! 🎬 If you encounter any issues, please check the troubleshooting section above or create a GitHub issue.


<h1 align="center">YouTube Video & Playlist Downloader</h1>
<h3 align="center">A powerful Python-based tool for downloading YouTube videos and playlists with customizable quality options.</h3>
<h3 align="center">Automatically merges video and audio for high-quality downloads.</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---

## 🚀 Features

- **Download Entire Playlists**: Automatically organizes videos into playlist folders.
- **Download Single Videos**: Works even with playlist URLs containing `&list=` parameters.
- **Multiple Quality Options**: Choose from 360p to 4K, or audio-only.
- **Automatic Merging**: FFmpeg integration for perfect video+audio synchronization.
- **Progress Tracking**: Real-time download progress display.
- **Error Handling**: Continues downloads even if some videos fail.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 📋 Prerequisites

- **Python 3.6 or higher** ([Download Python](https://www.python.org/downloads/))
  - During installation, check "Add Python to PATH".
- **FFmpeg** ([Download FFmpeg](https://www.gyan.dev/ffmpeg/builds/))
  - Required for high-quality video merging.

---

## 🔧 Installation

### 1. Download the Tool

```bash
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg (Required for High Quality)

**Windows:**
- Download FFmpeg from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
- Extract to `C:\ffmpeg\`
- Add `C:\ffmpeg\bin` to your system PATH:
  - Press Windows + S, type "environment variables"
  - Click "Edit the system environment variables"
  - Click "Environment Variables"
  - Under "System variables", find "Path" and click "Edit"
  - Click "New" and add: `C:\ffmpeg\bin`
  - Click OK → OK → OK

**Verify FFmpeg Installation:**
```bash
ffmpeg -version
```

---

## 🎯 Usage

### Download a Playlist

```bash
python youtube_playlist_downloader.py
```
- Enter the playlist URL (e.g., `https://www.youtube.com/playlist?list=YOUR_LIST_ID`)
- Choose download folder location
- Select video quality (1-7)

### Download a Single Video

```bash
python youtube_video_downloader.py
```
- Enter any YouTube video URL (even with `&list=` parameters)
- Choose download folder location
- Select video quality (1-7)

---

## ⚙️ Quality Options

When prompted, choose from:

1. **Best available (4K/1440p/1080p)** – Highest quality available
2. **1440p QHD** – 2560×1440 resolution
3. **1080p Full HD** – 1920×1080 resolution
4. **720p HD** – 1280×720 resolution (Recommended balance)
5. **480p** – Standard definition
6. **360p** – Low quality (small file size)
7. **Audio only** – MP3 audio only (192kbps)

---

## 📁 Output Structure

After downloading, your files will be organized as follows:

```
Your-Download-Folder/
├── Playlist Name 1/
│   ├── Video Title 1.mp4
│   ├── Video Title 2.mp4
│   └── ...
└── Individual Videos/
    ├── Single Video Title 1.mp4
    └── Single Video Title 2.mp4
```

- **Playlists**: Each playlist is saved in its own folder, named after the playlist.
- **Single Videos**: Videos downloaded individually are stored in the "Individual Videos" folder.
- **File Naming**: Each video is named after its YouTube title for easy identification.
- **Audio Only**: If you choose "Audio only," files are saved as `.mp3` in the same structure.

This organization helps you quickly find and manage your downloaded content.

---

## 📝 File Structure

```
youtube-downloader/
├── youtube_playlist_downloader.py   # Main playlist download script
├── youtube_video_downloader.py      # Single video download script
├── requirements.txt                 # Python dependencies
├── README.md                        # This documentation
└── ffmpeg/                          # FFmpeg binaries (optional)
    └── bin/
        ├── ffmpeg.exe
        ├── ffplay.exe
        └── ffprobe.exe
```

---

## 🔍 Troubleshooting

**Common Issues & Solutions:**

1. **"FFmpeg not found" error**
   - Install FFmpeg and add to PATH, or place `ffmpeg.exe` in the script folder.

2. **"HTTP Error 400: Bad Request"**
   - Update yt-dlp: `pip install --upgrade yt-dlp`

3. **Videos download as separate files**
   - Ensure FFmpeg is properly installed for merging.

4. **"Module not found" errors**
   - Install requirements: `pip install -r requirements.txt`

5. **Download stops or fails**
   - The script will automatically retry failed downloads.

**Need Help?**
- Create an issue on GitHub with:
  - The exact error message
  - Steps to reproduce the issue
  - Your operating system and Python version

---

## ⚠️ Legal Disclaimer

This tool is intended for personal use only. Please:
- Respect copyright laws in your country
- Follow YouTube's Terms of Service
- Only download content you have rights to access

The developers are not responsible for misuse of this tool.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

---

## 🆓 Free and Open Source

This is a free, open-source tool maintained by the community. If you find it useful, please give it a star on GitHub! ⭐

---

## ❗ Important Note

**FFmpeg Path Configuration:**  
Each Python script (`youtube_playlist_downloader.py` and `youtube_video_downloader.py`) contains a variable for the FFmpeg executable path.  
You **must** update this path to match the location of `ffmpeg.exe` on your system.  
Do **not** use the default or placeholder path.

**Example:**  
If you installed FFmpeg to `C:\ffmpeg\bin\ffmpeg.exe`, update the script as follows:

```python
ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
```

Make sure to use double backslashes (`\\`) or a raw string (`r"..."`) for Windows paths.

---

**Happy Downloading! 🎬 If you encounter any issues, please check the troubleshooting section above or create a GitHub issue.


from pytube import YouTube

def print_header():
    print("="*50)
    print("YouTube Video Downloader".center(50))
    print("="*50)

def get_available_resolutions(yt):
    resolutions = set()
    for stream in yt.streams.filter(progressive=True, file_extension="mp4"):
        resolutions.add(stream.resolution)
    return sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)

def select_resolution(resolutions):
    print("\nAvailable resolutions:")
    for i, res in enumerate(resolutions, 1):
        print(f"  [{i}] {res}")
    
    while True:
        choice = input("\nSelect a resolution (enter the number): ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(resolutions):
                return resolutions[index]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

try:
    print_header()

    # Prompt user to input the YT URL
    url = input("Enter the YouTube URL/Link: ")
    
    yt = YouTube(url)
    
    print_header()
    print(f"\nTitle: {yt.title}")
    print(f"Channel: {yt.author}")
    print(f"Views: {yt.views:,}")
    
    # Get available resolutions
    resolutions = get_available_resolutions(yt)
    
    if not resolutions:
        print("\nNo downloadable streams found.")
        exit()
    
    # Let user select resolution
    selected_resolution = select_resolution(resolutions)
    
    # Get the stream with the selected resolution
    yd = yt.streams.filter(progressive=True, file_extension="mp4", resolution=selected_resolution).first()
    
    if not yd:
        print(f"\nNo stream found for resolution {selected_resolution}")
        exit()
    
    # Download the video to the current directory
    print(f"\nDownloading {selected_resolution} resolution...")
    yd.download('./ytvideos')
    
    print("\nDownload complete!")

except Exception as e:
    print("\nAn error occurred:", str(e))

input("\nPress Enter to exit...")

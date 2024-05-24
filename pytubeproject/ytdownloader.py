from pytube import YouTube

try:
    # promopt user to input the YT URL
    url = input("Enter the YouTube URL/Link: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the current directory
    yd.download('./ytvideos')
    
    print("Download complete...")
except Exception as e:
    print("An error occurred:", str(e))

from pytube import YouTube
from sys import argv
import pytube.exceptions

link = input("Enter the link of the video: ")

try:
    yt = YouTube(link)
    print("Title of the video is: ", yt.title)
except pytube.exceptions.PytubeError as e:
    print(f"An error occurred: {e}")

choice = input("Are you sure you want to download this video? (y/n): ")
if choice =='y':
    yt.streams.get_highest_resolution().download('C:/Users/divya/Desktop/DownloadedVideos')
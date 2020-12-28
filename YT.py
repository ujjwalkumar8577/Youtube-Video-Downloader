from tkinter import *
from pytube import YouTube

# defining download function
def download():
    try:
        Label(root, text="Downloading ...", font="Consolas 12 bold").pack()
        root.update()
        YouTube(link.get()).streams.first().download()
        Label(root, text="Video downloaded successfully", font="Consolas 12 bold").pack()
    except Exception as e:
        Label(root, text="An error occured", font="Consolas 12 bold").pack()
        root.update()
        Label(root, text="Enter correct link", font="Consolas 12 bold").pack()

# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry("800x600")
# setting the title of the GUI
root.title("Youtube Video Downloader")
# creating the Label widgets
Label(root, text="Welcome!", font="Consolas 20 bold").pack()
Label(root, text="Enter the link below",font="Consolas 15 bold").pack()
# declaring StringVar type variable
link = StringVar()
# creating the Entry widget to get the link
Entry(root, textvariable=link, width=40).pack(pady=10)
# creating download button and calling the download function
Button(root, text="Download", command=download).pack()
# running the mainloop
root.mainloop()
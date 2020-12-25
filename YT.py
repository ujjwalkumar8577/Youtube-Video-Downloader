# importing tkinter
from tkinter import *
# importing YouTube module
from pytube import YouTube
# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry("400x400")
# setting the title of the GUI
root.title("Youtube Video Downloader")
# defining download function
def download():
    # using try and except to execute program without errors
    try:
        Label(root, text="Downloading ...", font="Consolas 12 bold").pack()
        #myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        #link.set("Video downloaded successfully")
        Label(root, text="Video downloaded successfully", font="Consolas 12 bold").pack()
    except Exception as e:
        Label(root, text="An error occured", font="Consolas 12 bold").pack()
        #myVar.set("Mistake")
        root.update()
        #link.set("Enter correct link")
        Label(root, text="Enter correct link", font="Consolas 12 bold").pack()

# created the Label widget to welcome user
Label(root, text="Welcome!", font="Consolas 20 bold").pack()
# declaring StringVar type variable
Label(root, text="Enter the link below",font="Consolas 15 bold").pack()
#myVar = StringVar()
# setting the default text to myVar
#myVar.set("Enter the link below")
# created the Entry widget to ask user to enter the url
#Entry(root, textvariable=myVar, width=40).pack(pady=10)
# declaring StringVar type variable
link = StringVar()
# created the Entry widget to get the link
Entry(root, textvariable=link, width=40).pack(pady=10)
# created and called the download function to download video
Button(root, text="Download", command=download).pack()
# running the mainloop
root.mainloop()
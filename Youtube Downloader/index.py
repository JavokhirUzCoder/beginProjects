from customtkinter import *

from pytube import YouTube
import time
from threading import Thread

window = CTk()
window.title("YouTube Video Downlaoder")
window.geometry("500x400")
window.resizable(False,False)
window.config(bg = "#000")



def Main():
    global result, url
    # result.set("")
    link = url.get()
    if link == "":
        result.set("Iltimos havolani kiriting")
    else:
        time.sleep(1)
        try:
            yt = YouTube(str(link))
            stream = yt.streams.get_highest_resolution()
            stream.download()

        except:
            result.set("Nimadir xato ketdi. Uzur 😔")
        else:
            result.set("Yuklanish nixoyasiga yetdi")


def Index():
    global result
    result.set("Iltimos kutib turing")

    work = Thread(target=Main)
    work.start()

titleX = CTkLabel(window, text= "Youtube Video Downloader",text_color="#fff", bg_color="#000", font = ("Arial", 30, "bold") ) 
titleX.place(x = 50, y = 0)

url = CTkEntry(window, placeholder_text="https://yotube.com/example/", font=("Arial", 20, "bold"), height=40, width=400)
url.place(x = 50, y = 50)

btn = CTkButton(window, text="Download", bg_color="#000", fg_color="green", font=("Arial", 23, "bold"),width=250, height=50, corner_radius=20, command=Index)
btn.place(x = 125, y = 120)

result = StringVar()
Result = CTkLabel(window, textvariable = result,text_color="#fff", bg_color="#000", font=("Arial", 25,"bold"))
Result.place(x = 100, y = 200)

window.mainloop()
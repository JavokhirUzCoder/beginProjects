from tkinter import filedialog as fd
from mutagen.easyid3 import EasyID3
from threading import Thread
from mutagen.id3 import ID3, APIC, error
from customtkinter import *

window = CTk()
window.geometry("700x400")
window.title("Music tagger")
window.config(bg="#000")
window.resizable(False, False)
# window.iconbitmap("rocket.ico")


path = ""

def starter():
    global path, clicktostart
    clicktostart.destroy()
    def change(path, title, album, artist, genre):
        alertText = StringVar()
        alertPy = CTkLabel(window, textvariable = alertText ,bg_color="#000",width = 100, text_color='white' ,font= ("Comic Sans MS", 20, "bold"))
        alertPy.place(x = 300, y = 200)
    
        try:
            audio = EasyID3(path)
            audio["title"] = title
            audio["album"] = album
            audio["artist"] = artist
            audio["genre"] = genre
            audio.save()
        except Exception as err:
            alertText.set("Error")
            print(err)
        else:
            alertText.set("O`zgartirildi")
        
        
        
        # typefile = path.split(".")[-1]
        # loc = path.split("/")
        # loc[-1] = "ᴍɪxᴇᴅ"
        # x = "/".join(loc)
        # x += f".{typefile}"
        # os.rename(path, x)


    fileTypes = (
        ("MP3 Files", "*.mp3"),
        # ("WAV Files", "*.wav"),
        # ("FLAC Files", "*.flac"),
        # ("M4A Files", "*.m4a"),
        # ("OGG Files", "*.ogg"),
        # ("WMA Files", "*.wma"),
        # ("AAC Files", "*.aac"),
        # ("AIFF Files", "*.aiff"),
        # ("ALAC Files", "*.alac"),
        # ("APE Files", "*.ape"),
        ("All files", "*.*"))

    
    try:
        path = fd.askopenfilename(filetypes=fileTypes)
    except:
        starter()
    else:

        title = CTkEntry(window,width=450, height = 40,bg_color="#000", font= ("Comic Sans MS", 14, "bold"), corner_radius=30, placeholder_text="Musiqaning nomini kiriting: ")
        title.place(x = 125, y = 30)
        album = CTkEntry(window,width=200, height = 40,bg_color="#000", font= ("Comic Sans MS", 14, "bold"), corner_radius=30, placeholder_text="Musiqaning albom nomini kiriting kiriting: ")
        album.place(x = 125, y = 80)
        artist = CTkEntry(window,width=200, height = 40,bg_color="#000", font= ("Comic Sans MS", 14, "bold"), corner_radius=30, placeholder_text="Musiqaning artisti nomini kiriting: ")
        artist.place(x = 375, y =80)
        genre = CTkEntry(window,width=200, height = 40,bg_color="#000", font= ("Comic Sans MS",14, "bold"), corner_radius=30, placeholder_text="Musiqaning janri kiring kiriting: ")
        genre.place(x = 125, y = 130)
        
        btn = CTkButton(window, text= "O`zgartirish", width=200,fg_color="green",border_width=2, height=40,bg_color="#000", corner_radius=30, command=lambda: change(path,title.get(), album.get(), artist.get(), genre.get()))
        btn.place(x=375, y = 130)

def MainWorker():
    work = Thread(target=starter)
    work.start()



clicktostart  = CTkButton(window, width=200, height = 70,bg_color="#000",fg_color="green",border_width=2, font= ("Comic Sans MS", 27, "bold"), corner_radius=10, text = "Tanlash", command=MainWorker)
clicktostart.place(x = 250, y =175)

window.mainloop()
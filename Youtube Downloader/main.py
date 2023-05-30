#  pip install eel
#  pip install eel[jinja2] 
from pytube import YouTube

import eel  
eel.init("web")



@eel.expose
def MainFunc(link):
    try:
        yt = YouTube(str(link))
        stream = yt.streams.get_highest_resolution()
        stream.download()

    except:
        return "Somthing went wrong!"
    else:
        return "Downloaded completed successfully"
eel.start("index.html", size =(400, 300))

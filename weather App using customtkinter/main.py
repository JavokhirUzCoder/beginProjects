from customtkinter import *
import requests
window = CTk()
window.geometry("340x420")
window.resizable(False, False)
window.config(bg="#2A9D8F")
GradusInt = StringVar()
Name = StringVar()
api_key = '688c8f05869ae74783e21f44039a996a'
def main(Country):
    global GradusInt,Name
    GradusInt.set("")
    Name.set("")
    if Country.lower() == "zarina":
        # GradusInt.set("")
        Name.set("I love You ❤️")
    else:
        try:
            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={Country}&units=imperial&APPID={api_key}")
            if weather_data.json()['cod'] == '404':
                Name.set("Bunday shahar mavjud emas")
            else:
                temp = round(weather_data.json()['main']['temp'])
        except:
            GradusInt.set("nimadir xato")
        else:
            GradusInt.set(f"{int((int(temp)-32 )*(5/9))} ºC")
            Name.set(f"{Country.upper()}")

searchbar = CTkEntry( window, width=312, height=67, bg_color="#2A9D8F", fg_color="#03071E", text_color="white", placeholder_text="Enter country name", corner_radius=50 , border_width=0)
searchbar.place(x = 14, y = 12)
button = CTkButton( window, text="Search",   width=147, height=49, bg_color="#2A9D8F", fg_color="#03071E", text_color="white",  corner_radius=50 , border_width=0, command=lambda:main(searchbar.get()) )
button.place(x = 97, y = 98)

gradus = CTkLabel(window, textvariable = GradusInt, font = ( "Arial",30, "bold"),text_color="white", width=340, height=30, fg_color="#2A9D8F", bg_color="#2A9D8F")
gradus.place(x = 0, y = 177)
NameCountry = CTkLabel(window, textvariable = Name, font = ( "Arial",24, "bold"),text_color="white", width=340, height=30, fg_color="#2A9D8F", bg_color="#2A9D8F")
NameCountry.place(x = 0, y = 328)



window.mainloop()
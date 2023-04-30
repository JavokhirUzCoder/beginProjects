# BUDILNIK dasturi



# Iltimos dastur islashi uchun ushbu kutubxonani o'rnating
# pip install playsound


import time
import os
from playsound import playsound
from datetime import datetime

now = datetime.now()

now = now.time()
nowtime = str(now).split(":")
nowtime[2] = nowtime[2][:2]

# nowtime[0] => dastur ishga tushgan vaqt soati
# nowtime[1] => dastur ishga tushgan vaqt minuti
# nowtime[2] => dastur ishga tushgan vaqt sekundi


os.system("cls")


print(f"Ayni damda vaqt => {str(now)[:8]}")
enteredtime = (input("Iltimos budilnik uchun vaqt kiriting (hh:mm:ss) : "))

ArrayofenteredTime = enteredtime.split(":")

enteredtimeHour = ArrayofenteredTime[0] # kiritilgan soat
enteredtimeMin = ArrayofenteredTime[1] # kiritilgan minut
enteredtimeSek = ArrayofenteredTime[2] # kiritilgan sekund

os.system("cls")
def trueTime(num):
    if int(num) >=10:
        return (num)
    else:
        return ("0" + (num))


while not(nowtime[0] == enteredtimeHour and nowtime[1] == enteredtimeMin and nowtime[2] == enteredtimeSek):
    print(f"Siz belgilagan vaqt: {enteredtimeHour}:{enteredtimeMin}:{enteredtimeSek} ")
    
    print(f"Ayni damdagi vaqt: {trueTime(nowtime[0])}:{trueTime(nowtime[1])}:{trueTime(nowtime[2])} ")
    
    nowtime[2] = str(int(nowtime[2]) + 1)
    
    if nowtime[2] == "59":
        nowtime[1] = str(int(nowtime[1]) + 1)
        nowtime[2] = "00"
        if nowtime[1] == "59":
            nowtime[0] = str(int(nowtime[0]) + 1)
            nowtime[1] = "00"
    time.sleep(1)
    os.system("cls")


for i in range(2):
    playsound('ring.mp3')
    print(f"Xizmatimizdan foydalanganingiz uchun raxmat.... 🙂🙂🙂🙂" )
    os.system("cls")
    os.system("cls")
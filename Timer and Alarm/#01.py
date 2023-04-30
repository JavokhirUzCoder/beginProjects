# Timer dasturi


# Iltimos dastur islashi uchun ushbu kutubxonani o'rnating
# pip install playsound


import time
import os
from playsound import playsound





timer = (input("Iltimos timer uchun vaqt kiriting (hh:mm:ss) : "))

aloneTimes = timer.split(":")


timerHour = int(aloneTimes[0])
timerMin = int(aloneTimes[1])
timerSek = int(aloneTimes[2])

os.system("cls")

#to'g'irlab beruvchi funksiya
def trueTime(num):
    if num >=10:
        return str(num)
    else:
        return ("0" + str(num))
        

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



while not( timerHour == 0 and timerMin == 0 and timerSek == 0):
    print (f"{bcolors.WARNING}{trueTime(timerHour)}:{trueTime(timerMin)}:{trueTime(timerSek)}")
    time.sleep(1)
    
    #Vaqtdan qarz olish
    if(timerSek == 0):
        if timerSek == 0:
            if timerMin == 0:
                timerHour -= 1
                timerMin = 59
            else:
                timerMin -=1
                timerSek = 59
    timerSek -=1
    os.system("cls")

for i in range(2):
    playsound('ring.mp3')
    os.system("cls")
os.system("cls")
print(f"{bcolors.HEADER}Xizmatimizdan foydalanganingiz uchun raxmat...." )
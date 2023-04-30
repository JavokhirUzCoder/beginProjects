import random


#email checker and Strong password generator
email = input("Email kiritib ko`ringchi:  ")

trueEmailSymbol = "@"
trueEmailMust = ".com"

trueEmailSymbolReal = True
DoNotUse = ["!", "#", "$", "%", "^", "&", "*", "(", ")", "+","-","/",","]
for i in DoNotUse:
    if i in email:
        trueEmailSymbolReal = False
        break

if email == email.lower() and (trueEmailSymbol in email) and (trueEmailMust in email) and trueEmailSymbolReal:
    print("Yes, This email is valid")
else:
    print("No, This email is invalid")


print("Section of Password")
#strong password

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


StrongPaswordIndex = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

#Xizmatchi funksiyalar
def isStrongPassword(passcode):
    m = False
    if len(passcode) < 8:
        m = False
    else:
        k = 0
        titleletter = 0
        for i in passcode:
            if i.isdigit() or i.isascii() :
                k = k + 1
            elif i.islower():
                k = k - 1
            elif i.isupper():
                titleletter = titleletter + 1
                
        if k < 6 and titleletter > 2:
            m = False
        else:
            m = True
    return m
            
def creatStrongPassword():
    x = int(input("Parolingiz uzunligi nechta bo`lsin (Iltimos 8 dan katta bo`lsin): "))
    password = ""
    if (x) > 7:
        for i in range(x):
            password = password + random.choice(StrongPaswordIndex)
    else:
        x = 0
        creatStrongPassword()
    return password

def IsLike():
    print("Sizga Yangi parol taqdim etiladi:  " + creatStrongPassword())
    if input("yuqoridagi parol sizga yoqdimi (Ha/Yo`q) ? >>> ").lower() == "ha":
        print("Xizmatimizdan foydalanganingiz uchun raxmat! 🙂🙂🙂")
    else: IsLike()
    
    
#Asosiy tana

Have_password = input("Sizda parol bormi (Ha/Yo`q) :  ").lower()

if Have_password == "ha":
    password = input("Parolingizni kiritingchi:  ")
    if isStrongPassword(password):
        print("Sizning parolingiz: " + password +" Ushbu parol yaroqli👍👍👍")
    else:
        if input("Sizning parolingiz yaroqli emas, Sizga yangi parol tayyorlab berishimizni xoxlaysizmi (Ha/Yo`q) : ").lower() == "ha":
            IsLike()
        else:
            print("Xizmatimizdan foydalanganingiz uchun raxmat! 🙂🙂🙂")
elif Have_password == "yo`q":
    if input("Parolingiz yo`q ekan, Sizga yangi parol tayyorlab berishimizni xoxlaysizmi (Ha/Yo`q) : ").lower() == "ha":
        IsLike()
    else:
        print("Xizmatimizdan foydalanganingiz uchun raxmat! 🙂🙂🙂")

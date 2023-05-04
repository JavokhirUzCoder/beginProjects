print("Belgilar haqida ")


Symbols = "!@#$%^&*()*+,-./"
Unli = "aeuio"
Undosh = "qwrtypsdfghjklmnbvcxz"


word = input("Text kiriting: ")

unliResult = 0
undoshResult = 0
symbolResult = 0

def unli_undosh_simvol_aniqla(text):
    global unliResult, undoshResult, symbolResult

    text = text.lower()
    for i in text:
        if i in Unli:
            unliResult += 1
        if i in Undosh:
            undoshResult += 1
        if i in Symbols:
            symbolResult += 1


unli_undosh_simvol_aniqla(word)

print("unlilar soni: ", unliResult)
print("undoshlarlar soni: ", undoshResult)
print("Simvollar soni: ", symbolResult)
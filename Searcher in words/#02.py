print("Sonlarni ajratib oluvchi dastur")

word = input()


def faqatsonlar(text):
    result = ""
    for i in text:
        if i.isdigit():
            result += i

    return result

print("Natija: ", faqatsonlar(word))
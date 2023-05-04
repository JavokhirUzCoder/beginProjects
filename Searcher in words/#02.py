def faqatsonlar(text):
    result = ""
    for i in text:
        if i.isdigit():
            result += i

    return result

print("Natija: ", faqatsonlar("2001 yil 4-aprel"))
print("Natija: ", faqatsonlar("1001uz1001"))

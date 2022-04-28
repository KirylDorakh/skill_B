def polindrom(text):
    text = text.lower().replace(" ", "")
    text_pol = text[::-1]
    if text_pol == text:
        return True
    else:
        return False


text = 'Кит на море не романтик'
i = polindrom(text)
print(i)
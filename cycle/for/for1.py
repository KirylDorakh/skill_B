text = ('aaabbccccdaa')

print(text)
new_text = ''
k = 0
print(range(len(text)))
print('len(text)', len(text))

for i in range(len(text)):
    if text[i] == text[i - 1] and i != (len(text) - 1):
        k += 1
        print(i)
    elif i == (len(text) - 1):
        k += 1
        new_text = new_text + text[i] + str(k)
        print("Finish")
    else:
        new_text = new_text + text[i - 1] + str(k)
        print(new_text)
        k = 1
print(new_text)

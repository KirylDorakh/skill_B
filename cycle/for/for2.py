text = ('aaabbccccdaa')

print(text)
new_text = ''
k = 0
last = text[0]

for i in text:
    if i == last:
        k += 1
    else:
        new_text += last + str(k)
        last = i
        k = 1
new_text += last + str(k)
print(new_text)
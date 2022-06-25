s = 'aaabbccccdaa'
result = s[0]
count = 1

for i in range(1, len(s) - 1):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += str(count) + s[i]
        count = 1

print(result + str(count + 1))


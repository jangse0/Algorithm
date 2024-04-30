str=input()
new=""
for i in range(len(str)):
    if str[i]<='Z':
        new+=chr(ord(str[i])+32)
    else:
        new+=chr(ord(str[i])-32)

print(new)
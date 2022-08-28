#!/usr/bin/python3

plainText = input().upper()

digest = ""

for i in range(0,len(plainText)):
    digest += chr(91 + 65-ord(plainText[i])-1)
print(digest)
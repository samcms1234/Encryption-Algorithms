#!/usr/bin/python3

def Caesar_cipher(n) -> str:
    Digest=""
    for i in n:
        if i.isupper():
            Digest+=chr(((ord(i)+3-65)%26)+65)
        elif i.islower():
             Digest+=chr(((ord(i)+3-97)%26)+97)
        else:
            Digest+=i
    return Digest
if __name__=="__main__":
    PlainText=input()
    print(Caesar_cipher(PlainText))

#!/usr/bin/python3

def Caesar_cipher_general(text,shift) -> str:
    Digest=""
    for i in text:
        if i.isupper():
            Digest+=chr(((ord(i)+shift-65)%26)+65)
        elif i.islower():
             Digest+=chr(((ord(i)+shift-97)%26)+97)
        else:
            Digest+=i
    return Digest
if __name__=="__main__":
    PlainText=input("Enter Plain Text: ")
    shift=int(input("Enter Shift: "))
    print(Caesar_cipher_general(PlainText,shift))
    

'''  The Beale ciphers are another example of a homophonic cipher.
    This is a story of buried treasure that was described in 1819–21
    by use of a ciphered text that was keyed to the Declaration of 
    Independence. Here each ciphertext character was represented by 
    a number. The number was determined by taking the plaintext 
    character and finding a word in the Declaration of Independence
    that started with that character and using the numerical 
    position of that word in the Declaration of Independence as 
    the encrypted form of that letter. Since many words in the 
    Declaration of Independence start with the same letter, the 
    encryption of that character could be any of the numbers 
    associated with the words in the Declaration of Independence 
    that start with that letter. Deciphering the encrypted text 
    character X (which is a number) is as simple as looking up 
    the Xth word of the Declaration of Independence and using the
    first letter of that word as the decrypted character. '''

def bealeCipher(n) -> str:
    

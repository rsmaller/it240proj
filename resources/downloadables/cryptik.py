#!/usr/bin/python3
# Vigenere ciphers a string from the user.

import os, sys
alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def cipherCombine(character, characterKey):
    try:
        return alphabet[(alphabet.index(character) + alphabet.index(characterKey)) % len(alphabet)]
    except Exception as error:
        return character

def decipherCombine(character, characterKey):
    if character not in alphabet:
        return character
    resultIndex = alphabet.index(character) - alphabet.index(characterKey)
    while (resultIndex > len(alphabet)):
        resultIndex -= len(alphabet)
    while (resultIndex < 0):
        resultIndex += len(alphabet)
    return alphabet[resultIndex]


def cipher(string, key):
    returnString = ""
    for index, character in enumerate(string):
        returnString += cipherCombine(character, key[index%len(key)])
    return returnString

def decipher(string, key):
    returnString = ""
    for index, character in enumerate(string):
        returnString += decipherCombine(character, key[index%len(key)])
    return returnString

def main():
    if len(sys.argv) < 3:
        print("Usage: cipher STRING KEY [-d]")
        quit()
    myString = sys.argv[1]
    myKey = sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3] == "-d":
        print(decipher(myString, myKey))
    else:
        myCipher = cipher(myString, myKey)
        print(myCipher)

main()
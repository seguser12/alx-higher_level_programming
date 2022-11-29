#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            chars = chr(ord(char) - 32)
        else:
            chars = char
        print(f'{chars}', end="")
    print('')

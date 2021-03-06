# -*- coding: utf-8 -*-

with open('lab1-1/lab1-1_input.txt','r') as f:
    ciphertext=f.read()
    dkey='CRYPTOGRAPHY'
    Lc=len(ciphertext)
    Ld=len(dkey)
    i=0
    plaintext=''
    for s in ciphertext:
        order=i%Ld
        tmp=(ord(s)-ord(dkey[order]))%26+ord('A')
        plaintext=plaintext+chr(tmp)
        i+=1
    print(plaintext)
    with open('lab1-1/lab1-1_output.txt','w') as g:
        g.write(plaintext)
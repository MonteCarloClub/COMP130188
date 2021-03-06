# -*- coding: utf-8 -*-

with open('lab1-1_1/lab1-1_1e.txt','r') as f1:
    read_data=f1.read()
    data_list=read_data.split()
    plaintext=data_list[0]
    ekey=data_list[1]
    Lp=len(plaintext)
    Le=len(ekey)
    i=0
    #ciphertext=[]
    ciphertext=''
    for s in plaintext:
        order=i%Le
        tmp=(ord(s)+ord(ekey[order])-2*ord('A'))%26+ord('A')
        #ciphertext.append(chr(tmp))
        ciphertext=ciphertext+chr(tmp)
        i+=1
    #print(''.join(ciphertext))
    print(ciphertext)
    with open('lab1-1_1/lab1-1_1ee.txt','w') as g1:
        g1.write(ciphertext)

with open('lab1-1_1/lab1-1_1d.txt','r') as f2:
    read_data=f2.read()
    data_list=read_data.split()
    ciphertext=data_list[0]
    dkey=data_list[1]
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
    with open('lab1-1_1/lab1-1_1dd.txt','w') as g2:
        g2.write(plaintext)
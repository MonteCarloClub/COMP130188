# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file,'r') as f:
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
        with open('lab1-1_output.txt','w') as g:
            g.write(plaintext)
        input('程序执行成功，按任意键退出：')
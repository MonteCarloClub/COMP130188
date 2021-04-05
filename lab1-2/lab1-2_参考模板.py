# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:17:40 2021

@author: Zhong Chongpeng
"""
#import sys

def decrypt(ciphertext, key):
    ciphertext = ciphertext.split()
    plaintext = ""
    """Returns plaintext decrypted by playfair cipher using key"""
    # WRITE YOUR CODE HERE!





    
    print(plaintext)
    return plaintext
        
     
def create_matrix_M(key):
    """Returns matrix created by playfair cipher using key"""
    # WRITE YOUR CODE HERE!
    







if __name__ == '__main__':
    # 测试代码
    decrypt("EQ VS ZT ES FS GZ","FUDAN")

    # 正式代码
    #file = sys.argv[1]
    #with open(file,'r') as f:
        #ciphertext = f.read()
        #plaintext = decrypt(ciphertext,'SECURITY')
        #with open('lab1-2_output.txt','w') as g:
            #g.write(plaintext)
        #input('程序执行成功，按任意键退出：')
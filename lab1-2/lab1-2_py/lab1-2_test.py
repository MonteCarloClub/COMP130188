# -*- coding: utf-8 -*-

def decrypt(ciphertext, key):
    ciphertext = ciphertext.split()
    plaintext = ''
    M = create_matrix_M(key)
    dict = {}
    for i in range(5):
        for j in range(5):
            # 创建 字母：M中对应行列号 的字典
            dict[M[i][j]] = [i,j]
    for s in ciphertext:
        # 首个字母在M中的行号
        idx00 = dict[s[0]][0]
        # 首个字母在M中的列号
        idx01 = dict[s[0]][1]
        # 第二个字母在M中的行号
        idx10 = dict[s[1]][0]
        # 第二个字母在M中的列号
        idx11 = dict[s[1]][1]
        # 若两字母行号相同
        if idx00 == idx10:
            s1 = M[idx00][(idx01+4)%5]
            s2 = M[idx10][(idx11+4)%5]
            plaintext = plaintext + s1 + s2 + ' '
            continue
        # 若两字母列号相同
        if idx01 == idx11:
            s1 = M[(idx00+4)%5][idx01]
            s2 = M[(idx10+4)%5][idx11]
            plaintext = plaintext + s1 + s2 + ' '
            continue
        # 两字母行号、列号均相同
        s1 = M[idx00][idx11]
        s2 = M[idx10][idx01]
        plaintext = plaintext + s1 + s2 + ' '
    # 去掉最后的空格
    plaintext.rstrip()
    print(plaintext)
    return plaintext
        

def create_matrix_M(key):
    # 用列表解析的方式构建一个5*5的嵌套列表
    M = [[0]*5 for i in range(5)]
    # ABC标注了字母是否已经被加入M
    ABC = [0]*26
    # 预先排除J
    ABC[ord('J')-ord('A')] = 2
    idx = 0
    # 将key中的包含的字母按原顺序加入M
    for s in key:
        i = ord(s) - ord('A')
        if ABC[i] == 0:
            M[idx//5][idx%5] = s
            ABC[i] = 1
            idx += 1
    # 将字母表中剩余的字母按顺序加入M
    for i in range(26):
        if ABC[i] == 0:
            M[idx//5][idx%5] = chr(i+ord('A'))
            idx += 1
    return M
        

if __name__ == '__main__':
    decrypt("EQ VS ZT ES FS GZ","FUDAN")
#include <iostream>

using namespace std;

char **CreateMatrix(char *key);
char *Decrypt(char *ciphertext,char *key);

int main()
{
    char ciphertext[] = "EQ VS ZT ES FS GZ";
    char key[] = "FUDAN";
    char *plaintext = Decrypt(ciphertext,key);
    cout << plaintext << endl;
    return 0;
}

//当返回值是二维数组时，函数名前加**
char **CreateMatrix(char *key)
{
    //使用new为二维数组开辟新的内存空间
    char **M = new char*[5];
    for (int i = 0; i < 5; i ++)
    {
        M[i] = new char[5];
    }
    //C++中新建数组必须初始化，否则可能出现意想不到的错误
    int ABC[26] = {0};
    ABC['J'-'A'] = 2;
    int idx = 0;

    for (int i = 0; key[i] != '\0'; i ++)
    {
        int ii = key[i] - 'A';
        if (ABC[ii] == 0)
        {
            M[idx/5][idx%5] = key[i];
            ABC[ii] = 1;
            idx ++;
        } 
    }

    for (int i = 0; i < 26; i ++)
    {
        if (ABC[i] == 0)
        {
            M[idx/5][idx%5] = char(i + 'A');
            idx ++;
        }
    }

    return M;
}

char *Decrypt(char *ciphertext,char *key)
{
    //新指针plaintext的初始化必须用static来修饰，使其成为全局变量
    char static *plaintext = ciphertext;
    //指针M的内存不必使用delete来释放，因为其本身就是局部变量
    char **M = CreateMatrix(key);
    int dic[26][2] = {0};

    for (int i = 0; i < 5; i ++)
    {
        for (int j = 0; j < 5; j ++)
        {
            dic[M[i][j]-'A'][0] = i;
            dic[M[i][j]-'A'][1] = j;
        }
    }

    for (int i = 0; plaintext[i] != '\0'; i += 3)
    {
        char s1 = plaintext[i], s2 = plaintext[i+1];
        int x1 = s1 - 'A', x2 = s2 - 'A';
        int idx00 = dic[x1][0], idx01 = dic[x1][1], 
            idx10 = dic[x2][0], idx11 = dic[x2][1];

        if (idx00 == idx10)
        {
            plaintext[i] = M[idx00][(idx01+4)%5];
            plaintext[i+1] = M[idx10][(idx11+4)%5];
            continue;
        }

        if (idx01 == idx11)
        {
            plaintext[i] = M[(idx00+4)%5][idx01];
            plaintext[i+1] = M[(idx10+4)%5][idx11];
            continue;
        }

        plaintext[i] = M[idx00][idx11];
        plaintext[i+1] = M[idx10][idx01];
    }
    
    return plaintext;
}
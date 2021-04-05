#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> CreateMatrix(string key);
string Decrypt(string ciphertext,string key);

int main()
{
    string ciphertext;
    ifstream input("lab1-2_input.txt");
    if (input)
    {
        //将文件input的第一行输入到ciphertext中
        getline(input,ciphertext);
        input.close();
    }

    string key = "SECURITY";
    string plaintext = Decrypt(ciphertext,key);
    cout << plaintext << endl;

    ofstream output("lab1-2_output.txt");
    if (output)
    {
        //将plaintext输入到文件output中
        output << plaintext << endl;
        output.close();
    }

    return 0;
}

//加密矩阵构建函数
vector<string> CreateMatrix(string key)
{
    //使用容器vector<string>存储字符矩阵M
    vector<string> M(5,"AAAAA");
    //数组ABC用来标记字母是否已经放入加密矩阵
    int ABC[26] = {0};
    ABC['J'-'A'] = 2;
    int idx = 0;

    //将密钥key中的字母按序放入加密矩阵
    for (auto &c : key)
    {
        int ii = c - 'A';
        if (ABC[ii] == 0)
        {
            M[idx/5][idx%5] = c;
            ABC[ii] = 1;
            idx ++;
        } 
    }

    //将字母表中剩余字母按序放入加密矩阵
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

//解密函数
string Decrypt(string ciphertext,string key)
{
    string plaintext = ciphertext;
    vector<string> M = CreateMatrix(key);

    //二维数组dic用来存储每个字母在加密矩阵中的行、列号
    int dic[26][2] = {0};
    for (int i = 0; i < 5; i ++)
    {
        for (int j = 0; j < 5; j ++)
        {
            dic[M[i][j]-'A'][0] = i;
            dic[M[i][j]-'A'][1] = j;
        }
    }
 
    //按规则对密文的所有字母对进行解密
    for (int i = 0; i < plaintext.size(); i += 3)
    {
        int x1 = plaintext[i] - 'A', x2 = plaintext[i+1] - 'A';
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
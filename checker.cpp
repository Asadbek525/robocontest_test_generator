// input.txt → avtor bergan input
// author.txt → avtor bergan output
// code.txt → userning kodi
// user.txt → user bergan output
#include <bits/stdc++.h>

#define ac 0xAC
#define wa 0xAD
#define pe 0xAE
#define tl 0xAF

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

ifstream input("input.txt");
ifstream output("author.txt");
ifstream user_output("user.txt");
ifstream code("code.txt");

void ret(int x) {
    input.close();
    output.close();
    user_output.close();
    code.close();
    exit(x);
}

int main()
{
    // a + b misol uchun checker
    try {
        ll ans, user_ans;
        output >> ans;
        user_output >> user_ans;

        // user javob sifatida 1 tadan ortiq son chiqargan taqdirda
        string s;
        if (user_output >> s) {
            ret(pe);
        }

        if (ans == user_ans) {
            ret(ac);
        }
        else {
            ret(wa);
        }

    }
    catch (const std::exception& e) {
        ret(pe);
    }
}

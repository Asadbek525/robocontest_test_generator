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

void close(int x) {
    input.close();
    output.close();
    user_output.close();
    code.close();
    exit(x);
}

int main()
{
    // necha xona aniqlikda ekanligini belgilash uchun
    // bunda 5 xonagacha aniqlikka tekshiriladi
    double max_error = 1e-5;

    // unutmang bu faqat bitta son chiqadigan holat uchun
    // output bir nechta son bo'lganda kodni o'zingizga moslashtiring
    try {
        double ans, user_ans;
        output >> ans;
        user_output >> user_ans;
        string s;
        if (user_output >> s) {
            close(pe);
        }

        if (abs(ans - user_ans) <= max_error) {
            close(ac);
        }
        else {
            close(wa);
        }
    }
    catch {
        close(pe);
    }
}
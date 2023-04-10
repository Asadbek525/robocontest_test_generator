#include <bits/stdc++.h>
using namespace std;


string to_4digit(int n) {
    string s = to_string(n);
    while (s.size() < 4) {
        s = "0" + s;
    }
    return s;
}

int main() {
    int start = 1;
    int end = 100;
    for (int i = start; i <= end; i++) {
        int n = rand() % 1000 + 1;
        ofstream f;
        f.open(to_4digit(i) + ".in");
        // input here
        f << n;
        f.close();
        f.open(to_4digit(i) + ".out");
        // output here
        f << "";
        f.close();
    }
}
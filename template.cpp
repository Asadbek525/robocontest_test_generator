#include <iostream>
#include <fstream>
#include <random>
#include <algorithm>

using namespace std;

#define int long long

int randint(int start, int end) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(start, end);
    return dis(gen);
}

string to_4digit(int n) {
    string s = to_string(n);
    while (s.size() < 4) {
        s = "0" + s;
    }
    return s;
}

signed main() {

    // check tests folder exists or not, if not, create it
    system("if [ ! -d tests ]; then mkdir tests; fi");
    // A + B example
    int from = 1;
    int to = 100;
    for (int i = from; i <= to; i++) {
        int A = randint(1, 1e9);
        int B = randint(1, 1e9);

        ofstream f;
        f.open("tests/" + to_4digit(i) + ".in");
        // input here
        f << A << " " << B << endl;
        f.close();
        f.open("tests/" +  to_4digit(i) + ".out");
        // output here
        f << A + B << endl;
        f.close();
    }
}

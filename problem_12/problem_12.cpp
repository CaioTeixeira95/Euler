#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int triangle_number(int before, int n) {
    return before + n;
}

int factors(int n) {
    int step = n % 2 ? 2 : 1;
    set<int> facs;
    for (int i = 1; i <= sqrt(n); i += step) {
        if (n % i == 0) {
            facs.insert(i);
            facs.insert(int(n / i));
        }
    }
    return facs.size();
}

int main() {
    int before = 0, n = 1;
    while (true) {
        int tn = triangle_number(before, n);
        cout << tn << endl;
        if (factors(tn) > 500) {
            cout << "Result: " << tn << endl;
            break;
        }
        before = tn;
        n++;
    }
    return 0;
}
